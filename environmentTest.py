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
env.getAllMap()
print p.coordinate.x,p.coordinate.y
env.move(p,"Down")
print p.coordinate.x,p.coordinate.y
print p.coordinate.key
print

env.getAllMap()
print p.coordinate.x,p.coordinate.y
env.move(p,"Up")
print p.coordinate.x,p.coordinate.y
print p.coordinate.key
env.getAllMap()
print

env.getAllMap()
print p.coordinate.x,p.coordinate.y
env.move(p,"Right")
print p.coordinate.x,p.coordinate.y
print p.coordinate.key
env.getAllMap()

print
env.getAllMap()
print p.coordinate.x,p.coordinate.y
env.move(p,"Left")
print p.coordinate.x,p.coordinate.y
print p.coordinate.key
env.getAllMap()
print


"""
# wall test
p2=PlayerFactory().new("p2","Ghost",0,-1,c2)
env.addPlayer(p2)
p2.point = 20
p2.level = 2
c1=Coordinate(39,10)
p1=PlayerFactory().new("p1","Pacman",0,1,c1) 
env.addPlayer(p1)
"""
env.move(p2,"Left")
print p2.coordinate.x,p2.coordinate.y
print p2.coordinate.key
env.getAllMap()
print

env.move(p2,"Up")
print p2.coordinate.x,p2.coordinate.y
print p2.coordinate.key
env.getAllMap()
print
"
env.move(p1,"Right")
print p1.coordinate.x,p1.coordinate.y
print p1.coordinate.key
env.getAllMap()
print
"
env.move(p1,"Down")
print p1.coordinate.x,p1.coordinate.y
print p1.coordinate.key
env.getAllMap()
print

# Forage Test
# ghost can not eat pacman
env.addForage(f1)
env.getAllMap()
print "point of p2 before eating forage",p2.point
env.move(p2,"Right")
env.getAllMap()
print "point of p2 after eating f1 ", p2.point
print p2.coordinate.x,p2.coordinate.y,p2.coordinate.key
print

#pacman can eat forage
c4 = Coordinate(38,10)
f3=ForageFactory().new("Apple",c4) 
print "before move p1 point:",p1.point
print "coordinates and key:",p1.coordinate.x,p1.coordinate.y,p1.coordinate.key
env.addForage(f3)
env.move(p1,"Up")
env.getAllMap()
print "after move p1 point:",p1.point
print "coordinates and key:",p1.coordinate.x,p1.coordinate.y,p1.coordinate.key
print

#pacman can not eat tomato
c4 = Coordinate(38,10)
f3=ForageFactory().new("Tomato",c4) 
print "before move p1 point:",p1.point
print "coordinates and key:",p1.coordinate.x,p1.coordinate.y,p1.coordinate.key
env.addForage(f3)
env.move(p1,"Up")
env.getAllMap()
print "after move p1 point:",p1.point
print "coordinates and key:",p1.coordinate.x,p1.coordinate.y,p1.coordinate.key
print
"""
# pacman can not eat ghost hataaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdad
c5 = Coordinate(11,10)
p4 = PlayerFactory().new("p4","Ghost",0,-1,c5)
env.addPlayer(p4)
env.getAllMap()
print
env.move(p,"Down")
env.getAllMap()
print p.coordinate.x,p.coordinate.y,p.coordinate.key
print
"""
# pacman can eat ghost
c5 = Coordinate(11,10)
p4 = PlayerFactory().new("p4","Ghost",0,-1,c5)
env.addPlayer(p4)
c6 = Coordinate(12,10)
p5 = PlayerFactory().new("p5","Pacman",40,3,c6)
env.addPlayer(p5)
print p5.level
env.getAllMap()
print "after move"
env.move(p5,"Up")
env.getAllMap()
print

# ghost can not eat pacman
c6 = Coordinate(12,10)
p5 = PlayerFactory().new("p5","Pacman",45,3,c6)
print p5.level
print p5.point
env.addPlayer(p5)
c7 = Coordinate(13,10)
p6 = PlayerFactory().new("p6","Ghost",10,-1,c7)
env.addPlayer(p6)
env.getAllMap()
print "after move"
env.move(p6,"Up")
env.getAllMap()
print "ghost point:", p5.point
print

# ghost can eat pacman and pacman dies
p.level=1
p.point=3
c8 = Coordinate(10,11)
p7 = PlayerFactory().new("p5","Ghost",15,-1,c8)
env.addPlayer(p7)
env.getAllMap()
env.move(p7,"Left")
print "after move"
env.getAllMap()
print p7.point

#ghost can eat pacman and pacman don't dies
p.level=2
p.point=15
c8 = Coordinate(10,11)
p7 = PlayerFactory().new("p5","Ghost",15,-1,c8)
env.addPlayer(p7)
env.getAllMap()
env.move(p7,"Left")
print "after move"
env.getAllMap()
print p7.point
print p.coordinate.x,p.coordinate.y,p.coordinate.key

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
