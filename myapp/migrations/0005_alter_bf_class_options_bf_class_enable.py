# Generated by Django 4.2.1 on 2023-05-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_bfm_class_bf_class_alter_bf_class_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bf_class',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Class'},
        ),
        migrations.AddField(
            model_name='bf_class',
            name='enable',
            field=models.BooleanField(default=True),
        ),
    ]