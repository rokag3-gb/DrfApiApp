from django.db import models

# Create your models here.

class mClass(models.Model):
    class Meta:
        db_table = 'class'
        verbose_name = '수업'
        verbose_name_plural = '수업'
    
    def __str__(self):  # admin에서 표시될 user 필드 정보 설정
        return self.title
    
    title = models.CharField(max_length=100, verbose_name='제목')
    place = models.CharField(max_length=300, verbose_name='장소')
    
    class KindChoices(models.TextChoices):
        TeamButFit = 'TBF', '팀버핏'
        ButFitPlay = 'BFP', '버핏플레이'
        Pilates = 'PIL', '필라테스'
    
    class CreditChoices(models.IntegerChoices):
        c05 = 50000, '5만원'
        c07 = 70000, '7만원'
        c10 = 100000, '10만원'
        c15 = 150000, '15만원'
    
    kind = models.CharField(max_length=10, choices=KindChoices.choices, verbose_name='종류')
    credit = models.IntegerField(choices=CreditChoices.choices, null=False, verbose_name='수업 가격(credit)')
    max_count = models.IntegerField(verbose_name='수업 정원')
    date = models.DateField(verbose_name='수업일')
    stime = models.TimeField(verbose_name='수업 시작시간')
    etime = models.TimeField(verbose_name='수업 종료시간')
    remark = models.TextField(max_length=1000, blank=True)
