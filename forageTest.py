from Forage import *
from Coordinate import *

c1=Coordinate(4,5)
c2=Coordinate(1,65)
c3=Coordinate(71,9)

f1=ForageFactory().new("Apple",c1)
f2=ForageFactory().new("Banana",c2)
f3=ForageFactory().new("Tomato",c3)

print "forage type:",f1.kind
print "forage point:",f1.point
print "forage coordinate-x:",f1.coordinate.x
print "forage coordinate-y:",f1.coordinate.y
print

print "forage type:",f2.kind
print "forage point:",f2.point
print "forage coordinate-x:",f2.coordinate.x
print "forage coordinate-y:",f2.coordinate.y
print

print "forage type:",f3.kind
print "forage point:",f3.point
print "forage coordinate-x:",f3.coordinate.x
print "forage coordinate-y:",f3.coordinate.y
print
