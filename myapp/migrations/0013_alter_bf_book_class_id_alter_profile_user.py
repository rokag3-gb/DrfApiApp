# Generated by Django 4.2.1 on 2023-05-23 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0012_alter_bf_book_book_date_alter_bf_book_cancel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bf_book',
            name='class_id',
            field=models.ForeignKey(db_column='class_id', on_delete=django.db.models.deletion.CASCADE, related_name='bf_Class', to='myapp.bf_class'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
