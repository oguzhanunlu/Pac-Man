from django.shortcuts import render
from forms import
# Create your views here.
def game(request):
    return
def signup(request):
    return
def signin(request):
    signinform = signinform()
    return render(request,'signin.html',{'form':signinform})
def mainpage(request):
    return render(request, 'mainpage.html')