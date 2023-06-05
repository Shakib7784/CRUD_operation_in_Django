from django.shortcuts import render,redirect
from ManageBook.forms import BookInfo
from ManageBook.models import Bookstore
# Create your views here.


def home(request):
    return render(request,"home.html")

def showbook(request):
    book = Bookstore.objects.all()
    res ={
        "book":book
    }
    return render(request,"showBook.html",res)

def storebook(request):
    if request.method=="POST":
        book = BookInfo(request.POST)
        if book.is_valid():
            book.save()
            return redirect("showbook")
    else :
        book = BookInfo()
        
    res ={
        "form":book
    }
    return render(request,"storeBook.html",res)
 
 
 
def edit(request,id):
     e = Bookstore.objects.get(pk = id)
     book = BookInfo(instance = e)
     if request.method=="POST":
        book = BookInfo(request.POST, instance=e)
        if book.is_valid():
            book.save()
            return redirect("showbook")
     res ={"form":book}
     return render(request,"storebook.html",res)
 
 
def deleteBook(request,id):
    b = Bookstore.objects.get(pk=id).delete()
    return redirect("showbook")