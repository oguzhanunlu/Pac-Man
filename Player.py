
from Environment import Environment as env

class Player(object):
    """
    Class definition of Player
    Beginner Player     :A player with point below 5
    Intermediate Player :A player with point between 5 and 35
    Pro Player          :A player with point above 35  
    """
        
    pass
        
class Ghost(Player):
    """
    A type of player.
    """
    def __init__(self,name, point,coordinate):
        """
        @param level: string, Beginner | Intermediate | Pro
        @param coordinate: Coordinate
        @return : A ghost instance 
        """
        self.name=name
        self.type="Ghost"
        self.point = point
        self.level = -1
        self.coordinate = coordinate      
        self.frame=[["Q" for i in xrange(11)] for i in xrange(11)]
    	            
    def canEatPlayer(self, player):
        if player.level == 3:
            return False
        return True
    
class Pacman(Player):
    """
    A type of player.
    """
    def __init__(self,name, point, level, coordinate):
        """
        @param level: Number, 1 |2 | 3
        @param coordinate: Coordinate
        @return : A player instance 
        """
        self.name=name
        self.type="Pacman"
        self.point = point
        self.level = level
        self.coordinate = coordinate       
        self.frame=[["Q" for i in xrange(11)] for i in xrange(11)]
    
    def levelChanger(self):
        if self.point<5:
            self.level = 1
        elif self.point>5 and self.point<35:
			self.level = 2			
        else:
            self.level = 3
#    def levelDown(self):	gerek kalmayabilir
#       self.level -= 1
    
    def canEatGhost(self, ghost):
        if self.level == 3:
            return True
        return False        
    
    def canEatForage(self, forage):
        if forage.kind == "Apple":
            return True
        elif forage.kind == "Banana" and not self.level == 1:
            return True
        elif forage.kind == "Tomato" and self.level == 3:
            return True
        return False
        
def Singleton(cls):
	'''generic python decorator to make any class
	singleton.'''
	_instances = {}	  # keep classname vs. instance
	def getinstance():
		'''if cls is not in _instances create it
		and store. return the stored instance'''
		if cls not in _instances:
			_instances[cls] = cls()
		return _instances[cls]
	return getinstance

@Singleton        
class PlayerFactory(object):
    """
    Factory design pattern to specify type of players.
    """
    def new(self,name, ptype,point,level, coordinate):  
        if ptype == "Ghost":
            return Ghost(name,point,coordinate)
        else:
            return Pacman(name,point,level, coordinate)
    
