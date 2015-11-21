class Player(object):
    """
    Class definition of Player
    Beginner Player     :A player with point below 5
    Intermediate Player :A player with point between 5 and 35
    Pro Player          :A player with point above 35  
    """
        
    def move(self, direction):
        """
        Moves user in given direction by 1 road, a square.
        @param direction: string, Up | Down | Right | Left
        """
        if direction == "Right":
            self.coordinate.x += 1
        elif direction == "Down":
            self.coordinate.y -= 1
        elif direction == "Left":
            self.coordinate.x -= 1
        else:
            self.coordinate.y += 1
        
class Ghost(Player):
    """
    A type of player.
    """
    def __init__(self, level, coordinate):
        """
        @param level: string, Beginner | Intermediate | Pro
        @param coordinate: Coordinate
        @return : A ghost instance 
        """
        self.level = level
        self.coordinate = coordinate      
    
    def canEatPlayer(self, player):
        if not player.level == 3:
            return False
        return True
    
class Pacman(Player):
    """
    A type of player.
    """
    def __init__(self, level, coordinate):
        """
        @param level: Number, 1 |2 | 3
        @param coordinate: Coordinate
        @return : A player instance 
        """
        self.level = level
        self.coordinate = coordinate       
    
    def levelUp(self):
        if self.level != 3:
            self.level += 1
    
    def levelDown(self):
        self.level -= 1
    
    def canEatGhost(self, ghost):
        if self.level == 3:
            return True
        return False        
    
    def canEatForage(self, forage):
        if forage.kind == "Apple":
            return True
        elif forage.kind == "Banana" and not self.level == 1:
            return True
        elif forage.kind == "Potato" and self.level == 3:
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
    def new(self, name, coordinate):  
        if name == "ghost":
            return Ghost(-1, coordinate)
        else:
            return Pacman(1, coordinate)
    
