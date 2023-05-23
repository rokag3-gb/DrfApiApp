from rest_framework.test import APITestCase
from rest_framework.views import status

from django.shortcuts import resolve_url
from django.urls import reverse
from ..models import *

# 테스트 코드는 작성하지 못하였습니다.

# class PhoneVerificationTestCase(APITestCase):
#     def setUp(self):
#         self.url_1 = '/accounts/verification'
#         self.url_2 = reverse('accounts:verification')
#         self.data = {"phone": "01012345678"}

#     def test_post_phone_number_success(self):
#         response = self.client.post(self.url_1, data=self.data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_post_phone_number_string_error(self):
#         data = {"phone": "010123456abc"}
#         response = self.client.post(self.url_2, data=data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)