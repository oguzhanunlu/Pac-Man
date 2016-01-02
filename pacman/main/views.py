from django.shortcuts import render
from django.http import HttpResponseRedirect

from socket import *
import cPickle as pickle

from .forms import *

# Create your views here.


def signin(request):

    form = SignInForm()
    return render(request, 'main/signin.html', {'form': form})


def signup(request):
    form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def mainpage(request):
    return render(request, 'main/mainpage.html')


def game(request):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("0.0.0.0", 50007))
    data = request.POST
    if not 'ptype' in data:
        name = data['name']
        s.send("signin "+name)
        response = s.recv(1000000)
        if response == "Player is created successfully.":
            response = pickle.loads(response)
            response['message']="yes"
            return render(request,'main/game.html',response)
    else:
        name = data['name']
        ptype = data['ptype']
        s.send("signup "+name +" "+ptype)
        response=s.recv(1000000)
        if response=="This username already exists.":
            return render(request,'main/game.html',{'message':"This username already exists."})
        else:
            response=pickle.loads(response)
            response['message']="yes"
            return render(request,'main/game.html',response)

    print 'data: '+data['name']
    context = {'data':data}
    return render(request, 'main/game.html', context)


