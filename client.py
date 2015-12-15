import socket
import time
import cPickle as pickle
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
fileinp=[]
while(1):
   
   if len(fileinp)>0:
      inp=fileinp[0]
      fileinp=fileinp[1:]
   else:
      inp  = raw_input("Enter command: ")
      if inp == '':
         continue  
   if inp[:4]=="File":
      fileHandler=open(inp[5:])
      fileinp=fileHandler.readlines()
      fileHandler.close()
      inp=fileinp[0]
      fileinp=fileinp[1:]
   
   command = inp.split(' ')
   s.send(inp)
   data=s.recv(1000000)
   if data=="Invalid command...":
      print data
   elif data=="Successfully closed.":
      print "Good bye..."
      s.close()
      break
   elif (data == "Player is created successfully."):
      s.send("getInfo")
      print 
      print "Welcome to game "+command[1]
   elif (data == "This username already exists."):
      print data
      continue
   elif data == "Olmussun yahu":
      print data
      s.close()
      break

   else: # handling move and possibility of dead
      data =  pickle.loads(data)
      if "message" in data:
         print "geldim XD"
         print data["message"]
         nmap= data["map"]
         for i in range (0,11):
            for j in range (0,11):
               print nmap[i][j][0].encode('UTF8'),
            print
         print "##########SCOREBOARD##########"
         for i in range(len(data["scoreboard"][0])):
            print data["scoreboard"][0][i], data["scoreboard"][1][i] 
         s.close()
      else:
         nmap= data["map"]
         for i in range (0,11):
            for j in range (0,11):
               print nmap[i][j][0].encode('UTF8'),
            print
         print "##########SCOREBOARD##########"
         for i in range(len(data["scoreboard"][0])):
            print data["scoreboard"][0][i], data["scoreboard"][1][i] 
         
         #print 'Received', data

