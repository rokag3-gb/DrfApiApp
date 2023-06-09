# Generated by Django 4.2.1 on 2023-05-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_bf_class_enable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bf_class',
            name='credit',
            field=models.IntegerField(choices=[(50000, '5만원'), (70000, '7만원'), (100000, '10만원'), (150000, '15만원')], verbose_name='수업 가격(credit)'),
        ),
        migrations.AlterField(
            model_name='bf_class',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='수업일'),
        ),
        migrations.AlterField(
            model_name='bf_class',
            name='etime',
            field=models.TimeField(blank=True, null=True, verbose_name='수업 종료시간'),
        ),
        migrations.AlterField(
            model_name='bf_class',
            name='max_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='수업 정원'),
        ),
        migrations.AlterField(
            model_name='bf_class',
            name='remark',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='bf_class',
            name='stime',
            field=models.TimeField(blank=True, null=True, verbose_name='수업 시작시간'),
        ),
    ]
