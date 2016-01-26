from django.shortcuts import render
from django.http import HttpResponse

from socket import *
import cPickle as pickle
import json
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


def quit(request):
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

    if request.is_ajax():
        dir = request.build_absolute_uri()[-1]
        print "dir", dir
        s.send(dir)
        response = s.recv(1000000)
        print response
        if response == "Olmussun yahu":
            message = "<b><center>Life hurts a lot more than death. Have a nice day.</center></b>"
            return HttpResponse(message)

        response = json.loads(response)
        for i in range(0,len(response['map'])):
            for j in range(0,len(response['map'][i])):
                response['map'][i][j] = response['map'][i][j].encode('utf8')

        for i in range (0,len(response['scoreboard'][0])):
            response['scoreboard'][0][i] = response['scoreboard'][0][i].encode('utf8')

        return HttpResponse(json.dumps(response))

    if request.method == "GET":
        dir = request.build_absolute_uri()[-1]
        s.send(dir)
        response = s.recv(1000000)
        response = json.loads(response)
        for i in range(0,len(response['map'])):
            for j in range(0,len(response['map'][i])):
                response['map'][i][j] = response['map'][i][j].encode('utf8')

        for i in range (0,len(response['scoreboard'][0])):
            response['scoreboard'][0][i] = response['scoreboard'][0][i].encode('utf8')

        if response['message'] == "Olmussun yahu":
            message = "<b>Life hurts a lot more than death. Have a nice day.</b>"
            return render(request, 'main/game.html', {'message': message})
        else:
            return render(request, 'main/game.html', response)
    else:

        data = request.POST


        if not 'ptype' in data: # signin
            name = data['name']

            s.send("signin "+name)
            response = s.recv(1000000)
            response = json.loads(response)
            for i in range(0,len(response['map'])):
                for j in range(0,len(response['map'][i])):
                    response['map'][i][j] = response['map'][i][j].encode('utf8')

            for i in range (0,len(response['scoreboard'][0])):
                response['scoreboard'][0][i] = response['scoreboard'][0][i].encode('utf8')
            response['scoreboard'] = zip(response['scoreboard'][0], response['scoreboard'][1])

            if response['message'] == "Player is created successfully.":
                sessions[name]=s
                request.session["oguzhan"]=name
                print "ress: ", response
                response['message']="yes"
                response['range'] = range(11)
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
                response=json.loads(response)

                for i in range(0,len(response['map'])):
                    for j in range(0,len(response['map'][i])):
                        response['map'][i][j] = response['map'][i][j].encode('utf8')

                #print 'map-> ', response['map']
                for i in range (0,len(response['scoreboard'][0])):
                    response['scoreboard'][0][i] = response['scoreboard'][0][i].encode('utf8')
                response['scoreboard'] = zip(response['scoreboard'][0], response['scoreboard'][1])

                print "resp: ", response
                response['message']="yes"
                print "burada"
                print response['map'][0]
                response['range'] = range(11)
                return render(request,'main/game.html',response)
        #s.close()
        print 'data: '+data['name']
        context = {'data':data}
        return render(request, 'main/game.html', context)


