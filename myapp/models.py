from django.db import models
import computed_property
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime

# Create your models here.

class bf_Class(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name='제목')
    place = models.CharField(max_length=300, null=False, verbose_name='장소')
    
    class KindChoices(models.TextChoices):
        TeamButFit = 'TBF', '팀버핏'
        ButFitPlay = 'BFP', '버핏플레이'
        Pilates = 'PIL', '필라테스'
    
    class CreditChoices(models.IntegerChoices):
        c05 = 50000, '5만원'
        c07 = 70000, '7만원'
        c10 = 100000, '10만원'
        c15 = 150000, '15만원'
    
    kind = models.CharField(max_length=10, choices=KindChoices.choices, null=False, verbose_name='종류')
    enable = models.BooleanField(default=True, null=False, verbose_name='활성')
    credit = models.IntegerField(choices=CreditChoices.choices, null=False, verbose_name='수업 가격(credit)')
    max_count = models.IntegerField(blank=True, null=True, verbose_name='수업 정원')

    date = models.DateField(blank=True, null=True, verbose_name='수업 시작일')
    stime = models.TimeField(blank=True, null=True, verbose_name='수업 시작시간')
    etime = models.TimeField(blank=True, null=True, verbose_name='수업 종료시간')
    remark = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'bf_Class'
        verbose_name = 'Class'
        verbose_name_plural = 'Class'

    def __str__(self):  # Django admin에서 표시될 필드 설정
        return str(self.pk) + ' / ' + self.title + ' / ' + self.place + ' / ' + self.date.strftime("%Y-%m-%d")

###################################################################################################

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="User", on_delete=models.CASCADE, db_column="user_id")
    phone_number = models.CharField(max_length=100, blank=True, null=True, verbose_name='연락처')
    birth_date = models.DateField(null=True, blank=True, verbose_name='생년월일')

    class Meta:
        db_table = 'Profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):  # Django admin에서 표시될 필드 설정
        return '[' + str(self.pk) + ']' + self.user.first_name + ' ' + self.user.last_name

###################################################################################################

class bf_UserCredit(models.Model):
    id = models.AutoField(primary_key=True)
    pay_date = models.DateField(blank=False, null=False, verbose_name='크레딧 구매일')
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = models.IntegerField(blank=False, null=False, default=1, verbose_name='user_id')
    place = models.CharField(max_length=300, blank=True, null=True, verbose_name='장소(optional)')
    credit = models.IntegerField(null=False, verbose_name='credit(원)')
    enable = models.BooleanField(default=True, null=False, verbose_name='활성')
    expire_period = computed_property.ComputedIntegerField(compute_from='calc_expire_period')
    expire_date = computed_property.ComputedDateField(compute_from='calc_expire_date', null=True)
    # remark = models.TextField(max_length=1000, blank=True, null=True)

    def calc_expire_period(self):
        expire_period=30

        if self.credit < 100000: # 10만원 미만
            expire_period=30
        elif self.credit >= 100000 and self.credit < 200000: # 10만원 이상 ~ 20만원 미만
            expire_period=60
        elif self.credit >= 200000 and self.credit < 300000: # 20만원 이상 ~ 30만원 미만
            expire_period=90
        elif self.credit >= 300000 and self.credit < 400000: # 30만원 이상 ~ 40만원 미만
            expire_period=120
        elif self.credit >= 400000: # 40만원 이상
            expire_period=150
        
        return expire_period
    
    def calc_expire_date(self):
        expire_date=datetime.datetime.today() + datetime.timedelta(days=self.calc_expire_period())

        return expire_date
    
    class Meta:
        db_table = 'bf_UserCredit'
        verbose_name = 'UserCredit'
        verbose_name_plural = 'UserCredit'
    
    def __str__(self):  # Django admin에서 표시될 필드 설정
        return str(self.id) + ' / ' + self.pay_date.strftime("%Y-%m-%d") + ' / ' + str(self.credit) + ' / ' + self.expire_date.strftime("%Y-%m-%d")

###################################################################################################

class bf_Book(models.Model):
    id = models.AutoField(primary_key=True)
    book_date = models.DateTimeField(blank=False, null=False, verbose_name='예약일')

    # user_id = models.ForeignKey("auth_user", related_name="user", on_delete=models.CASCADE, db_column="user_id")
    # user_id = models.IntegerField(blank=False, null=False, verbose_name='user_id')
    # class_id = models.IntegerField(blank=False, null=False, verbose_name='class_id')
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, db_column="user_id")
    class_id = models.ForeignKey(bf_Class, related_name="bf_Class", on_delete=models.CASCADE, db_column="class_id")

    enable = models.BooleanField(default=True, null=False, verbose_name='활성')
    spent_credit = models.IntegerField(blank=False, null=False, verbose_name='차감된 크레딧')

    cancel_date = models.DateTimeField(blank=True, null=True, verbose_name='예약취소일')
    refund_credit = models.IntegerField(blank=True, null=True, verbose_name='환불된 크레딧')

    class Meta:
        db_table = 'bf_Book'
        verbose_name = 'Book'
        verbose_name_plural = 'Book'

    def __str__(self):  # Django admin에서 표시될 필드 설정
        return 'Book_id: ' + str(self.pk) + ' / ' + self.book_date.strftime("%Y-%m-%d") + ' / ' + self.user_id.phone_number + ' / ' + self.user_id.user.first_name + ' ' + self.user_id.user.last_name

###################################################################################################

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         bf_UserCredit.objects.create(user=instance)