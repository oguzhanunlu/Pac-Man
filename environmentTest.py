from Environment import *
from Player import *
from Forage import *
from Coordinate import *
from Road import *

'''
0) environment create
1) player add-delete
2) forage add-delete
3) playerWindow
4) player move / 4 direction & eat player, ghost or forage / harekete engel seylerin kontrolu
5) get scoreboard
6) save & load

'''

#######################################
# environment create
#######################################

env = Environment()
env.mapGenerator()
env.getAllMap()

#######################################
# player add-delete
#######################################

#add player test p1 can not be added but p2 can be added
c1=Coordinate(1,1)
c2=Coordinate(0,0)
p1=PlayerFactory().new("p1","Pacman",0,1,c1) 
env.addPlayer(p1) 
env.getAllMap()
print
p2=PlayerFactory().new("p2","Ghost",0,-1,c2)
env.addPlayer(p2)
p2.point = 20
p2.level = 2
env.getAllMap()
print
env.deletePlayer(p2)
env.getAllMap()
print

#######################################
# forage add-delete
#######################################
c0 = Coordinate(0,1)
f1=ForageFactory().new("Apple",c0)
env.addForage(f1)
env.getAllMap()
print

f2=ForageFactory().new("Banana",c1) # this can not be added
env.addForage(f2)
env.getAllMap()
print

#delete forage test
env.deleteForage(f1)
env.getAllMap()
print

#######################################
# player window
#######################################

c1 = Coordinate(10,10)
p = PlayerFactory().new("p","Pacman",0,1,c1) 
p.point = 15
p.level = 2
env.addPlayer(p)
env.getAllMap()
env.getMap(p,5,5)
print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
#######################################
# player move
#######################################

# 4 direction test
"""
env.move(p,"Right")
env.getAllMap()
print

env.move(p,"Left")
env.getAllMap()
print

env.move(p,"Down")
env.getAllMap()
print
"""
env.getAllMap()
print p.coordinate.x,p.coordinate.y
env.move(p,"Down")
print
env.getAllMap()
print p.coordinate.x,p.coordinate.y
env.move(p,"Down")
env.getAllMap()
print
env.move(p,"Down")
env.getAllMap()
print
env.move(p,"Up")
env.getAllMap()
print
print p.coordinate.x,p.coordinate.y
print env.map[p.coordinate.x+5][p.coordinate.y]
print p.coordinate.x,p.coordinate.y
env.getAllMap()
print
"""
# wall test
env.move(p2,"Left")
env.getAllMap()
print
env.move(p2,"Up")
env.getAllMap()
print

# eat forage 
env.move(p2,"Right")
env.getAllMap()
print "point of p2 after eating f1 ", p2.point
print

# can not eat tomato
c4 = Coordinate(1,0)
f3=ForageFactory().new("Tomato",c4) 
env.addForage(f3)
env.move(p2,"Down")
env.getAllMap()
print

# pacman can not eat ghost
c5 = Coordinate(21,10)
p4 = PlayerFactory().new("p4","Ghost",0,-1,c5)
env.move(p,"Down")
env.getAllMap()
print

# pacman can eat ghost
c6 = Coordinate(22,10)
p5 = PlayerFactory().new("p5","Pacman",40,3,c6)
env.move(p,"Up")
env.getAllMap()
print

# ghost can not eat pacman
c7 = Coordinate(23,10)
p6 = PlayerFactory().new("p6","Ghost",0,-1,c7)
env.move(p5,"Up")
env.getAllMap()
print

# ghost can eat pacman
env.deleteForage(f3) # clean (1,0)
c8 = Coordinate(1,0)
p7 = PlayerFactory().new("p5","Pacman",40,3,c8)
env.move(p,"Up")
env.getAllMap()
print


#######################################
# get scoreboard
#######################################

c3 = Coordinate(30,10)
p3 = PlayerFactory().new("p3","Pacman",0,1,c3)
p3.point = 5 
env.addPlayer(p3)
env.getScoreBoard()

#######################################
# save & load
#######################################
env.save()

env1 = Environment()
env1.load()

env.getAllMap()
print 
env1.getAllMap()
print

env.printDict(env.playerDict)
print
env1.printDict(env1.playerDict)
print
env.printDict(env.forageDict)
print
env1.printDict(env1.forageDict)
"""
