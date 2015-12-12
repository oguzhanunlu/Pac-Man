#! /usr/bin/python
from Player import *
from Environment import *
from Coordinate import *
from Road import *
from Forage import *
from threading import *
import socket
import time
import json



def randomCoordinate(kind):
    while(1):
      i = random.randrange(0,4)
      i *= 10
      j = random.randrange(0,40)
      try:
         if(kind == "Ghost"):
            if(env.map[i][j] == "r" and env.map[i][j+1] != "P" and env.map[i][j+2] != "P" and env.map[i][j-1] != "P" and env.map[i][j-2] != "P" and env.map[i-1][j] != "P" and env.map[i-2][j] != "P" and env.map[i+1][j] != "P" and env.map[i+2][j] != "P" and env.map[i+1][j+1] != "P" and env.map[i-1][j+1] != "P" and env.map[i-1][j-1] != "P" and env.map[i+1][j-1] != "P"):
               c=Coordinate(i,j)
         else:
            if(env.map[i][j] == "r" and env.map[i][j+1] != "G" and env.map[i][j+2] != "P" and env.map[i][j-1] != "G" and env.map[i][j-2] != "P" and env.map[i-1][j] != "G" and env.map[i-2][j] != "G" and env.map[i+1][j] != "G" and env.map[i+2][j] != "G" and env.map[i+1][j+1] != "P" and env.map[i-1][j+1] != "G" and env.map[i-1][j-1] != "G" and env.map[i+1][j-1] != "G"):
               c=Coordinate(i,j)
         return c       
      except error:
         continue

class Agent(Thread):
   try:
      env =Environment()
      env.mapGenerator()
   except:
      print "geldim XD"
   def __init__(self, connection, address, server):
      Thread.__init__(self)
      self.connection = connection
      self.address = address
      self.server = server
         
         
         
   def run(self):
      while 1:
         self.inp = self.connection.recv(10000)
         self.command = self.inp.split(' ')
         if self.command[0] =="Quit":
            #save game
            self.connection.send("Successfully closed.")
            break
         elif (self.command[0] =="SignUp" ):
            self.username = self.command[1]
            self.kind = self.command[2]
            if self.username in env.usernames:
               self.connection.send("This username already exists.")
            else:
               self.c = randomCoordinate(self.kind)
               print self.c.x,self.c.y
               self.p = PlayerFactory().new(self.username,self.kind,0,1,self.c)
               env.addPlayer(self.p)
               #conn.send("Player with name "+p.name+" is created with type "+p.type+" successfully.")
               self.a={"map":env.getMap(p,5,5),"scoreboard":env.getScoreBoard()}
               self.out = json.dumps(self.a,indent = 4)
               self.connection.send(self.out)
         else:      
            self.a={"map":env.map,"scoreboard":env.getScoreBoard()}
            self.out = json.dumps(self.a)
            if not self.out: break
            self.connection.send(self.out)

      self.connection.close()
   
   
                  




class Server:
   def __init__(self):
      self.host = ''
      self.port = 50007
      self.backlog = 5
      self.size = 10000
      self.server = None
      self.agents = []

   def start_server(self):
      self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      self.server.bind((self.host,self.port))
      self.server.listen(self.backlog)
      while 1:
         conn, addr = self.server.accept()
         agent = Agent(conn,addr,self)
         self.agents.append(agent)        
         agent.start()


if __name__ =='__main__':
   server = Server()
   server.start_server() 
      

"""
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
#print 'Connected by', addr
while 1:
   inp = conn.recv(10000)
   command = inp.split(' ')
   if command[0] =="Quit":
      #save game
      conn.send("Successfully closed.")
      break
   elif (command[0] =="SignUp" ):
      username = command[1]
      kind = command[2]
      if username in env.usernames:
         conn.send("This username already exists.")
      else:
         c = randomCoordinate(kind)
         print c.x,c.y
         p = PlayerFactory().new(username,kind,0,1,c)
         env.addPlayer(p)
         #conn.send("Player with name "+p.name+" is created with type "+p.type+" successfully.")
         a={"map":env.getMap(p,5,5),"scoreboard":env.getScoreBoard()}
         out = json.dumps(a,indent = 4)
         conn.send(out)
   else:      
      a={"map":env.map,"scoreboard":env.getScoreBoard()}
      out = json.dumps(a)
      if not out: break
      conn.send(out)

conn.close()
"""
