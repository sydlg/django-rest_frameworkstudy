from django.shortcuts import render
from .serializers import BookSerializer, BookModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile, Book
from rest_framework import mixins, generics, viewsets
from rest_framework.permissions import BasePermission


# 1.使用Serializer
class BookAPIView1(APIView):
	"""
	使用Serializer
	"""

	def get(self, requset, format=None):

		APIKey = self.request.query_params.get("apikey", 0)
		developer = UserProfile.objects.filter(APIkey=APIKey).first()

		if developer:
			balance = developer.money
			if balance > 0:
				isbn = self.request.query_params.get('isbn', 0)

				books = Book.objects.filter(isbn=int(isbn))

				books_serializer = BookSerializer(books, many=True)

				developer.money -= 1

				developer.save()

				return Response(books_serializer.data)
			else:
				return Response("余额不足")

		else:
			return Response("APIKey输入错误")


# 2.使用ModelSerializer
class BookAPIView2(APIView):
	"""
	使用Serializer
	"""

	def get(self, requset, format=None):

		APIKey = self.request.query_params.get("apikey", 0)
		developer = UserProfile.objects.filter(APIkey=APIKey).first()

		if developer:
			balance = developer.money
			if balance > 0:
				isbn = self.request.query_params.get('isbn', 0)

				books = Book.objects.filter(isbn=int(isbn))

				books_serializer = BookModelSerializer(books, many=True)

				developer.money -= 1

				developer.save()

				return Response(books_serializer.data)
			else:
				return Response("余额不足")

		else:
			return Response("APIKey输入错误")


# Django REST framework视图三层封装
# 用mixins.ListModelMixin+GenericAPIView的方式实现视图封装
class BookMixinView1(mixins.ListModelMixin, generics.GenericAPIView):
	queryset = Book.objects.all()

	serializer_class = BookModelSerializer

	def get(self, request, *args, **kwargs):  # 如果这里不加get函数，代表默认不支持get访问这个api，所以必须加上
		APIKey = self.request.query_params.get("apikey", 0)
		developer = UserProfile.objects.filter(APIkey=APIKey).first()
		if developer:
			balance = developer.money
			if balance > 0:
				isbn = self.request.query_params.get("isbn", 0)

				developer.money -= 1

				developer.save()

				self.queryset = Book.objects.filter(isbn=int(isbn))
				return self.list(request, *args, **kwargs)

			else:

				return Response("余额不足")

		else:

			return Response("APIKey输入错误")


# Django REST framework视图三层封装
# 使用generics.ListAPIView  在上一个基础上封装get方法
class BookMixinView2(generics.ListAPIView):
	queryset = Book.objects.all()

	serializer_class = BookModelSerializer

	def get(self, request, *args, **kwargs):  # 如果这里不加get函数，代表默认不支持get访问这个api，所以必须加上
		APIKey = self.request.query_params.get("apikey", 0)
		developer = UserProfile.objects.filter(APIkey=APIKey).first()
		if developer:
			balance = developer.money
			if balance > 0:
				isbn = self.request.query_params.get("isbn", 0)

				developer.money -= 1

				developer.save()

				self.queryset = Book.objects.filter(isbn=int(isbn))
				return self.list(request, *args, **kwargs)

			else:

				return Response("余额不足")

		else:

			return Response("APIKey输入错误")


# Django REST framework视图三层封装
# 用viewsets+Router的方式实现视图封装
class IsDeveloper(BasePermission):
	message = '查无此人啊'

	def has_permission(self, request, view):

		APIKey = request.query_params.get("apikey", 0)

		developer = UserProfile.objects.filter(APIkey=APIKey).first()

		if developer:

			return True

		else:

			print(self.message)

			return False


class EnoughMoney(BasePermission):
	message = "兄弟，又到了需要充钱的时候！好开心啊！"

	def has_permission(self, request, view):

		APIKey = request.query_params.get("apikey", 0)

		developer = UserProfile.objects.filter(APIkey=APIKey).first()

		balance = developer.money

		if balance > 0:

			developer.money -= 1

			developer.save()

			return True

		else:

			return False


class BookModelViewSet(viewsets.ModelViewSet):
	authentication_classes = []

	permission_classes = [IsDeveloper, EnoughMoney]

	queryset = Book.objects.all()

	serializer_class = BookModelSerializer

	def get_queryset(self):
		isbn = self.request.query_params.get("isbn", 0)

		books = Book.objects.filter(isbn=int(isbn))

		queryset = books

		return queryset
