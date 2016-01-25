#! /usr/bin/python
from Player import *
from Environment import *
from Coordinate import *
from Road import *
from Forage import *
from threading import *
import socket
import time
import cPickle as pickle
import json


class Agent(Thread):
   try:
      env =Environment()
      env.mapGenerator()
      counter=0
      while 1:
         j = random.randrange(0,1000)
         k= random.randrange(0,1000)         
         if env.map[j][k]=='r':
            c=Coordinate(j,k)
            forage=ForageFactory().new("Tomato",c)
            env.addForage(forage)
            counter+=1
            if counter ==500:
               break
      counter=0           
      while 1:
         j = random.randrange(0,1000)
         k= random.randrange(0,1000)
         if env.map[j][k]=='r':
            c=Coordinate(j,k)
            forage=ForageFactory().new("Banana",c)
            env.addForage(forage)
            counter+=1
            if counter ==1000:
               break
      counter=0           
      while 1:
         j = random.randrange(0,1000)
         k= random.randrange(0,1000)
         if env.map[j][k]=='r':
            c=Coordinate(j,k)
            forage=ForageFactory().new("Apple",c)
            env.addForage(forage)
            counter+=1
            if counter ==2000:
               break        
      #env.getAllMap()             
   except:
      print "geldim XD"
   def __init__(self, connection, address, server):
      Thread.__init__(self)
      print "selam dunyali, ben bir threadim"
      self.connection = connection
      self.address = address
      self.server = server
      self.cont = False
   def randomCoordinate(self,kind):
       while(1):
         i = random.randrange(0,100)
         i *= 10
         j = random.randrange(0,1000)
         if i<2 or i>997 or j<2 or j > 997:
            continue
         if(kind == "Ghost"):
         
            if(self.env.map[i][j] == "r" and self.env.map[i][j+1] != "P" and self.env.map[i][j+2] != "P" and self.env.map[i][j-1] != "P" and self.env.map[i][j-2] != "P" and self.env.map[i-1][j] != "P" and self.env.map[i-2][j] != "P" and self.env.map[i+1][j] != "P" and self.env.map[i+2][j] != "P" and self.env.map[i+1][j+1] != "P" and self.env.map[i-1][j+1] != "P" and self.env.map[i-1][j-1] != "P" and self.env.map[i+1][j-1] != "P"):
               self.c=Coordinate(i,j)
         else:
            if(self.env.map[i][j] == "r" and self.env.map[i][j+1] != "G" and self.env.map[i][j+2] != "P" and self.env.map[i][j-1] != "G" and self.env.map[i][j-2] != "P" and self.env.map[i-1][j] != "G" and self.env.map[i-2][j] != "G" and self.env.map[i+1][j] != "G" and self.env.map[i+2][j] != "G" and self.env.map[i+1][j+1] != "P" and self.env.map[i-1][j+1] != "G" and self.env.map[i-1][j-1] != "G" and self.env.map[i+1][j-1] != "G"):
               self.c=Coordinate(i,j)
         return self.c       


   def run(self):
      while 1:
         self.inp = self.connection.recv(1000000)
         if not self.inp:
            continue
         self.command = self.inp.split()
         
         if self.command[0] =="quit":
            with open("pickle/"+self.p.name,'wb') as f:
               self.pdict = vars(self.p)
               self.c = Coordinate(self.pdict['coordinate'].x, self.pdict['coordinate'].y)
               del self.pdict['coordinate']
               json.dump(vars(self.p),f)
            self.p.coordinate = self.c
            self.env.deletePlayer(self.p)
            self.connection.send("Successfully closed.")
            break

         elif (self.command[0] =="signin" ):
            with open("pickle/"+self.command[1], 'rb') as f:
               self.pdict = json.load(f)
            self.kind = self.pdict['type']
            while 1:
                self.c = self.randomCoordinate(self.kind)
                if self.env.map[self.c.x][self.c.y]=='r':
                    break
            self.p = PlayerFactory().new(self.pdict['name'],self.kind,self.pdict['point'],self.pdict['level'],self.c)   
            self.env.addPlayer(self.p)
            #self.connection.send("Logged in.")
            self.a={"message": "Player is created successfully.", "map":self.env.getMap(self.p,5,5),"scoreboard":self.env.getScoreBoard()}
            print self.a["map"]
            self.out = json.dumps(self.a)
            self.connection.send(self.out)            
         
         elif (self.command[0] =="signup" ):
            self.username = self.command[1]
            self.kind = self.command[2]
            if self.username in self.env.usernames:
               self.connection.send("This username already exists.")
               print "ayni isim"
               continue
            else:
               while 1:
                  self.c = self.randomCoordinate(self.command[2])
                  if self.env.map[self.c.x][self.c.y]=='r':
                     break               
               
               print self.c.x,self.c.y
               
               self.p = PlayerFactory().new(self.username,self.kind,0,1,self.c)
               print "buarafa"
               self.env.addPlayer(self.p)
             #  self.connection.send("Player is created successfully.")
               print "geldi"
               self.a={"map":self.env.getMap(self.p,5,5),"scoreboard":self.env.getScoreBoard()}
               print self.a["map"]
               try:                
                  self.out = json.dumps(self.a)
                  self.connection.send(self.out)
                  print "data gitti"
               except:
                  print "olmadi......"
         
         elif self.command[0]=="l" or self.command[0]=="r" or self.command[0]=="u" or self.command[0]=="d" or self.command[0]=="/":
            self.dead = False
            #print "before move"
            #print self.p.type, self.p.coordinate.x, self.p.coordinate.y
            #print
            self.p.frame=[["Q" for i in xrange(11)] for i in xrange(11)]
            try:
               if self.env.playerDict[str(self.p.coordinate.x)+'.'+str(self.p.coordinate.y)].type != self.p.type:
                  self.dead = True
            except:      
               self.connection.send("Olmussun yahu")
               self.env.usernames.remove(self.p.name)
               self.a={"message":"Ogren de gel :) AHAHAHA","map":self.env.getMap(self.p,5,5),"scoreboard":self.env.getScoreBoard()}
               #print self.a["map"]
               
            if not self.dead :   
               if self.command[0] != "/":
                   self.env.move(self.p,self.command[0])
               #print "after move"
               #print self.p.name,self.p.type, self.p.coordinate.x, self.p.coordinate.y
               #print "bizim canimiz yanmaz gardas"
               self.a={"message":"in","map":self.env.getMap(self.p,5,5),"scoreboard":self.env.getScoreBoard()}
               #print self.a["map"]
               self.out= json.dumps(self.a)
               self.connection.send(self.out)
                        
         
         else:
            try:
               self.connection.send("Invalid command...")
            except socket.error:
               print "Game is over for this user..."
               break
      self.connection.close()
   
   
                  




class Server:
   def __init__(self):
      self.host = ''
      self.port = 50007
      self.backlog = 5
      self.size = 1000000
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

