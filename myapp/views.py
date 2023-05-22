from django.http import Http404
from django.shortcuts import render
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import ClassSerializer, UserCreditSerializer, BookSerializer
from .models import bf_Class, bf_UserCredit, bf_Book

# Create your views here.

# @api_view: 함수 기반 보기 작업을 위한 데코레이터
# APIView: 클래스 기반 보기 작업을 위한 클래스

#########################################################################

class ClassListAPI(APIView):
    def get(self, request):
        queryset = bf_Class.objects.all()
        print(queryset)
        serializer = ClassSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassDetail(APIView):
    def get_object(self, pk):
        try:
            return bf_Class.objects.get(pk=pk)
        except bf_Class.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        single_data = self.get_object(pk)
        serializer = ClassSerializer(single_data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        single_data = self.get_object(pk)
        serializer = ClassSerializer(single_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        single_data = self.get_object(pk)
        single_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#########################################################################

class UserCreditListAPI(APIView):
    def get(self, request):
        queryset = bf_UserCredit.objects.all()
        print(queryset)
        serializer = UserCreditSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = UserCreditSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreditDetail(APIView):
    def get_object(self, pk):
        try:
            return bf_UserCredit.objects.get(pk=pk)
        except bf_UserCredit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        single_data = self.get_object(pk)
        serializer = UserCreditSerializer(single_data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        single_data = self.get_object(pk)
        serializer = UserCreditSerializer(single_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        single_data = self.get_object(pk)
        single_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#########################################################################

class BookListAPI(APIView):
    def get(self, request):
        queryset = bf_Book.objects.all()
        print(queryset)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get_object(self, pk):
        try:
            return bf_Book.objects.get(pk=pk)
        except bf_Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        single_data = self.get_object(pk)
        serializer = BookSerializer(single_data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        single_data = self.get_object(pk)
        serializer = BookSerializer(single_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     single_data = self.get_object(pk)
    #     single_data.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

#########################################################################

# @api_view(['GET', 'POST'])
# def Class_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         queryset = bf_Class.objects.all()
#         print(queryset)
#         serializer = ClassSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ClassSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)