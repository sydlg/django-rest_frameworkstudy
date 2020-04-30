from django.shortcuts import render,redirect,HttpResponse
from rest_framework.views import APIView

# Create your views here.
class IndexView(APIView):

    """

    首页

    """

    # authentication_classes = []
	#
    # permission_classes = []
    # 前端添加{
    #
    #   “Authorization”:” JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2l
    #
    #   kIjoxLCJ1c2VybmFtZSI6InJvb3QiLCJleHAiOjE1NTE0NzYwNTcsImVtYWlsIjoiIn0.xSx
    #
    #   BU438PBYEx-jyv-lLi5DBrLQRzF-vxn1biBwg6aM”
    #
    # }字段
    def get(self,request):

        print(request)

        return HttpResponse('首页')