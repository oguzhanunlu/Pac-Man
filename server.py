#! /usr/bin/python
from Player import *
from Environment import *
from Coordinate import *
from Road import *
from Forage import *

import socket
import time
import json


env =Environment()
env.mapGenerator()

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

