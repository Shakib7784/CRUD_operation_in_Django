from django import forms
from ManageBook.models import Bookstore

class BookInfo(forms.ModelForm):
    class Meta:
        model = Bookstore
        fields = ["id","Book_name","Author_name","category"]
        labels={
            "id":"id",
            "Book Name":  "Book_name",
            "Authon name": "Author_name",
            "category" : "category",
        }