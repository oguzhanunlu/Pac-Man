from Environment import *
from Player import *
from Forage import *
from Coordinate import *
from Road import *
c1=Coordinate(3,3)
c2=Coordinate(3,1)

env=Environment()
env.map = [['X','r','X','X'],['r','r','X','X'],['r','X','r','r'],['r','r','r','X']]
#add forage tests f1 can not be added but f2 can be added
print env.map
print

f1=ForageFactory().new("apple",c1)
env.addForage(f1)
print env.map
print

f2=ForageFactory().new("banana",c2)
env.addForage(f2)
print env.map
print

#delete forage test
env.deleteForage(f2)
print env.map
print

#add player test p1 can not be added but p2 can be added
p1=PlayerFactory().new("p1","pacman",0,1,c1) 
env.addPlayer(p1)
print env.map
print

p2=PlayerFactory().new("p2","pacman",0,1,c2)
env.addPlayer(p2)
print env.map

#movement of pacman
p2.move("Right")

#delete pllayer test
env.deletePlayer(p2)
print env.map
print




