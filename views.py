from django.shortcuts import render
from django.http import HttpResponse
from myfirstwebapp.models import *

def home(request):
    #return HttpResponse("<h1>Hi I am a Django Server. Nice to meet you all. Welcome to Django basic training.</h1>")


    peoples = [
        {'Name' : 'Akshay', 'Age' : 20},
        {'Name' : 'Abijit', 'Age' : 17},
        {'Name' : 'Amit', 'Age' : 19},
        {'Name' : 'Aishwarya', 'Age' : 18},
        {'Name' : 'Komal', 'Age' : 14},
        {'Name' : 'Khushbu', 'Age' : 20},
        {'Name' : 'Rohan', 'Age' : 39},
        {'Name' : 'Shekhar', 'Age' : 32},
        {'Name' : 'Gokul', 'Age' : 45},
        {'Name' : 'Prashant', 'Age' : 42},
    ]
    return render(request, "home/index.html", context={'peoples' : peoples})
    

    
def ab(request):
    
    return render(request, "home/about.html")



def success(request):
    return HttpResponse("<h1>This is a success page</h1>")

 