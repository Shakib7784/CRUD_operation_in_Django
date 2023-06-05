from django.contrib import admin
from ManageBook.models import Bookstore
# Register your models here.


class book(admin.ModelAdmin):
    list_display=["id","Book_name","Author_name","category","first_pub","last_pub"]
admin.site.register(Bookstore,book)