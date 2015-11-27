#Movement will be tested with Environment
from Forage import *
from Player import *
from Coordinate import *

c1=Coordinate(3,9)
c2=Coordinate(7,2)
p1=PlayerFactory().new("p1","ghost",0,-1,c1)
p2=PlayerFactory().new("p2","pacman",0,1,c2)
f1=ForageFactory().new("apple",c2)
f2=ForageFactory().new("banana",c2)
f3=ForageFactory().new("tomato",c2)
#initialization test
print "player name:",p1.name
print "player type:",p1.type
print "player point:",p1.point
print "player level:",p1.level
print "player coordinate-x:",p1.coordinate.x
print "player coordinate-y:",p1.coordinate.y
print

print "player name:",p2.name
print "player type:",p2.type
print "player point:",p2.point
print "player level:",p2.level
print "player coordinate-x:",p2.coordinate.x
print "player coordinate-y:",p2.coordinate.y
print
#test for levelchanger,canEatGhost and Forage
print "before increasing point:","point:",p2.point,"level:",p2.level
print "whether pacman can eat ghost:",p2.canEatGhost(p1)
print "whether pacman can eat apple:",p2.canEatForage(f1)
print "whether pacman can eat banana:",p2.canEatForage(f2)
print "whether pacman can eat tomato:",p2.canEatForage(f3)
print
p2.point=40
p2.levelChanger()
print "after increasing point:","point:",p2.point,"level:",p2.level
print "whether pacman can eat ghost:",p2.canEatGhost(p1)
print "whether pacman can eat apple:",p2.canEatForage(f1)
print "whether pacman can eat banana:",p2.canEatForage(f2)
print "whether pacman can eat tomato:",p2.canEatForage(f3)
print
p2.point-=12
p2.levelChanger()
print "after decreasing point:","point:",p2.point,"level:",p2.level
print "whether pacman can eat ghost:",p2.canEatGhost(p1)
print "whether pacman can eat apple:",p2.canEatForage(f1)
print "whether pacman can eat banana:",p2.canEatForage(f2)
print "whether pacman can eat tomato:",p2.canEatForage(f3)
print
#whether ghost can eat pacman
print "whether ghost can eat pacman:",p1.canEatPlayer(p2)
#ghost can not eat level 3 pacman 
p2.point=50
p2.levelChanger()
print "whether ghost can eat pacman:",p1.canEatPlayer(p2)




