from django.db.models import F
from django.http import Http404, HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views import View
from rest_framework.decorators import api_view
from django.core.exceptions import ValidationError
import json
from datetime import datetime, timedelta

from .serializers import ClassSerializer, UserCreditSerializer, BookSerializer, UserBookSerializer
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
        body_unicode = request.body.decode('utf-8')
        json_data = json.loads(body_unicode)
        user_id = json_data.get('user_id')
        class_id = json_data.get('class_id')
        print('user_id=' + str(user_id) + ', class_id=' + str(class_id))

        queryset = bf_Book.objects.filter(user_id=user_id, class_id=class_id)

        if queryset.exists():
            raise ValidationError("해당 수업에 같은 유저가 이미 존재하기 때문에 신청할 수 없습니다!")
        # dup_check(json_data.get('user_id'), json_data.get('class_id'))

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def dup_check(user_id, class_id):
        # queryset = bf_Book.objects.filter(user_id=user_id, class_id=class_id)
        # if queryset.exists():
        #     raise ValidationError("해당 수업에 같은 유저가 이미 존재하기 때문에 신청할 수 없습니다!")
        # return queryset.count()

        # req=HttpRequest(request)
        # req.__init__()
        # body_data=req.body.decode('utf-8')
        # json_data=json.loads(body_data)

        # user_id=json_data.get('user_id')
        # class_id=json_data.get('class_id')
        # user_id = self.request.query_params.get('user_id')
        # class_id = self.request.query_params.get('class_id')
        
        # queryset.filter(user_id=user_id, class_id=class_id)
        # try:
        # except bf_Book.DoesNotExist:
        #     raise Http404


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
        body_unicode = request.body.decode('utf-8')
        json_data = json.loads(body_unicode)
        user_id = json_data.get('user_id')
        class_id = json_data.get('class_id')
        print('user_id=' + str(user_id) + ', class_id=' + str(class_id))

        single_data = self.get_object(pk)
        single_class = bf_Class.objects.get(pk=class_id)

        if single_class.date == datetime.now().date():
            raise ValidationError("수업 당일 취소 불가!")
        
        if single_class.date - timedelta(days=3) > datetime.now().date(): # 수업 시작 기준 3일전 크레딧 전액 환불
            #json_data['refund_credit'] = single_data.spent_credit
            single_data.refund_credit = single_data.spent_credit

        if single_class.date - timedelta(days=1) > datetime.now().date(): # 수업 시간 기준 1일전 크레딧 50% 환불
            single_data.refund_credit = single_data.spent_credit / 50

        # new_body = json.dumps(json_data).encode('utf-8')
        # new_request = HttpRequest()
        # new_request.method = request.method
        # new_request.body = new_body
        # new_request.headers = request.headers

        serializer = BookSerializer(single_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put_cancel(self, request, pk, format=None):
    #     single_data = self.get_object(pk)
    #     serializer = BookSerializer(single_data, data=request.data)
    #     # single_data.
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        single_data = self.get_object(pk)
        single_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#########################################################################

class UserBookListAPI(APIView):
    def get(self, request):
        queryset = bf_Book.objects.filter(book_date__gte='2023-05-23', book_date__lte='2023-05-23')
        # .select_related('bf_Class').filter(class_id=F('Class__id'))
        # .filter(book_date__gte='2023-05-22', book_date__lte='2023-05-23')
        print(queryset)
        serializer = UserBookSerializer(queryset, many=True)
        return Response(serializer.data)

# select  b.id, b.book_date, b.enable, b.spent_credit, b.cancel_date, b.refund_credit
#         , c.*
# from    bf_Book b
#         inner join bf_Class c on c.id = b.class_id
# where   b.user_id = {user_id}
# and     b.book_date between {sdate} and {edate}
# and     예약, 취소, 수업종료, 수업삭제

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