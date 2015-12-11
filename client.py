import socket
import time
import json
HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while(1):
   inp  = raw_input("Enter command: ")
   command = inp.split(' ')
   s.send(inp)
   data=s.recv(10000)
   if data=="Successfully closed.":
      print "Good bye..."
      s.close()
      break
   elif (data == "Player with name "+command[1]+" is created with type "+command[2]+" successfully."):
      print 
      print "Welcome to game "+command[1] 
   else:
      data =  json.loads(data)
      nmap= data["map"]
      for i in range (0,11):
         for j in range (0,11):
            print nmap[i][j][0].encode('UTF8'),
         print
      #print 'Received', data

