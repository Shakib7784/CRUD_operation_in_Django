from django.db import models

# Create your models here.

class Bookstore(models.Model):
    choice = [
        ("Classics","classics"),
        ("crime","crime"),
        ("horror","horro"),
        ("fantasy","fantasy"),
        ("History","History")
    ]
    id = models.IntegerField(primary_key=True)
    Book_name = models.CharField(max_length=40)
    Author_name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=choice)
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.Book_name