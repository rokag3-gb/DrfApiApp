from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import bf_Class, bf_UserCredit, bf_Book


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = bf_Class # bf_Class 모델 사용
        fields = '__all__' # 모든 필드 포함


class UserCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = bf_UserCredit
        fields = '__all__' # 모든 필드 포함


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = bf_Book
        fields = '__all__' # 모든 필드 포함
