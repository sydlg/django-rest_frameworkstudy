#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 12:18
# @Site    : 
# @File    : serializers.py

from rest_framework import serializers
from .models import UserProfile, Book


# 1.Serializer序列化,如果字段过多要写会严重影响开发效率
class BookSerializer(serializers.Serializer):
	title = serializers.CharField(required=True, max_length=100)
	isbn = serializers.CharField(required=True, max_length=100)
	author = serializers.CharField(required=True, max_length=100)
	publish = serializers.CharField(required=True, max_length=100)
	rate = serializers.FloatField(default=0)


# 2.ModelSerializer序列化可以直接全选，一般直接使用这个
class BookModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = "__all__"  # 表的所有字段序列化
# fields = ('title', 'isbn', 'author') 指定序列化某些字段
