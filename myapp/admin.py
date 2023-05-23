from django.contrib import admin
from .models import bf_Class, bf_UserCredit, bf_Book

# Register your models here.

admin.site.register(bf_Class)
admin.site.register(bf_UserCredit)

class bf_BookAdmin(admin.ModelAdmin):
    search_fields = ['id', 'book_date', 'first_name']

admin.site.register(bf_Book, bf_BookAdmin)