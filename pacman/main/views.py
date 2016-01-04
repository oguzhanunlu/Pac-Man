from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest

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


def qquit(request):
    global sessions
    s=sessions[request.session["oguzhan"]]
    s.send("quit")
    del sessions[request.session["oguzhan"]]
    del request.session["oguzhan"]

    return render(request, 'main/quit.html')


sessions={}
def game(request):
    global sessions
    s=None
    print "Hilli,", sessions.keys()
    if "oguzhan" in request.session.keys():
        s=sessions[request.session["oguzhan"]]
    else:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(("127.0.0.1", 50007))
    if request.method == "GET":
        dir = request.build_absolute_uri()[-1]
        s.send(dir)
        response = s.recv(1000000)
        response = pickle.loads(response)
        if response['message'] == "Olmussun yahu":
            message = "<b>Life hurts a lot more than death. Have a nice day.</b>"
            return render(request, 'main/game.html', {'message': message})
        else:
            #data = request.GET
            #print "datammm: ", data
            #s.send(data['dir'][0])

            #data = pickle.loads(data)
            #print "data: ", data
            #data['message'] = "yes"
            #context = {'data':data}
            return render(request, 'main/game.html', response)
    else:

        data = request.POST


        if not 'ptype' in data: # signin
            name = data['name']

            s.send("signin "+name)
            response = s.recv(1000000)
            response = pickle.loads(response)
            print "asasd ", response
            if response['message'] == "Player is created successfully.":
                sessions[name]=s
                request.session["oguzhan"]=name
                print "ress: ", response
                response['message']="yes"
                return render(request,'main/game.html',response)
        else: # signup
            name = data['name']
            ptype = data['ptype']
            s.send("signup "+name +" "+ptype)
            response=s.recv(1000000)
            if response == "This username already exists.":
                return render(request, 'main/game.html', {'message': "This username already exists."})
            else:
                sessions[name]=s
                request.session["oguzhan"]=name
                response=pickle.loads(response)
                print "resp: ", response
                response['message']="yes"
                return render(request,'main/game.html',response)
        #s.close()
        print 'data: '+data['name']
        context = {'data':data}
        return render(request, 'main/game.html', context)


