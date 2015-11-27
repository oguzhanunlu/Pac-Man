#TODO level up-down 

import Environment as env

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
        self.type="ghost"
        self.point = 0
        self.level = -1
        self.coordinate = coordinate      
    
    def move(self, direction):
        """
        Moves user in given direction by 1 road, a square.
        @param direction: string, Up | Down | Right | Left
        """
        if direction == "Right":
            if self.coordinate.x + 1 == 1000:
                pass
            elif env.map[self.coordinate.x+1][self.coordinate.y] == 'G':
                pass
            elif env.map[self.coordinate.x+1][self.coordinate.y] == 'P':
                if self.canEatPlayer(env.playerDict[str(x+1)+'.'+str(y)]):
                    self.point += env.playerDict[str(x+1)+'.'+str(y)].point 
                    deletePlayer(env.playerDict[str(x+1)+'.'+str(y)])
                else:
                    env.playerDict[str(x+1)+'.'+str(y)].point+=self.point
                    deletePlayer(self.coordinate.key)
            elif env.map[self.coordinate.x+1][self.coordinate.y] == 'A' or  env.map[self.coordinate.x+1][self.coordinate.y] == 'B' or  env.map[self.coordinate.x+1][self.coordinate.y] == 'T':
                pass
            else:
                self.coordinate.x += 1
            
        elif direction == "Down":
            if self.coordinate.y + 1 == 1000:
                pass
            elif env.map[self.coordinate.x][self.coordinate.y+1] == 'G':
                pass
            elif env.map[self.coordinate.x][self.coordinate.y+1] == 'P':
                if self.canEatPlayer(env.playerDict[str(x)+'.'+str(y+1)]):
                    self.point += env.playerDict[str(x)+'.'+str(y+1)].point 
                    deletePlayer(env.playerDict[str(x)+'.'+str(y+1)])
                else:
                    env.playerDict[str(x)+'.'+str(y+1)].point+=self.point
                    deletePlayer(self.coordinate.key)
            elif env.map[self.coordinate.x][self.coordinate.y+1] == 'A' or  env.map[self.coordinate.x][self.coordinate.y+1] == 'B' or  env.map[self.coordinate.x][self.coordinate.y+1] == 'T':
                pass
            else:
                self.coordinate.y += 1
            
        elif direction == "Left":
            if self.coordinate.x - 1 < 0:
                pass
            elif env.map[self.coordinate.x-1][self.coordinate.y] == 'G':
                pass
            elif env.map[self.coordinate.x-1][self.coordinate.y] == 'P':
                if self.canEatPlayer(env.playerDict[str(x-1)+'.'+str(y)]):
                    self.point += env.playerDict[str(x-1)+'.'+str(y)].point 
                    deletePlayer(env.playerDict[str(x-1)+'.'+str(y)])
                else:
                    env.playerDict[str(x-1)+'.'+str(y)].point+=self.point
                    deletePlayer(self.coordinate.key)
            elif env.map[self.coordinate.x-1][self.coordinate.y] == 'A' or  env.map[self.coordinate.x-1][self.coordinate.y] == 'B' or  env.map[self.coordinate.x-1][self.coordinate.y] == 'T':
                pass
            else:
                self.coordinate.x -= 1
            
        else:
            if self.coordinate.y - 1 == -1:
                pass
            elif env.map[self.coordinate.x][self.coordinate.y-1] == 'G':
                pass
            elif env.map[self.coordinate.x][self.coordinate.y-1] == 'P':
                if self.canEatPlayer(env.playerDict[str(x)+'.'+str(y-1)]):
                    self.point += env.playerDict[str(x)+'.'+str(y-1)].point 
                    deletePlayer(env.playerDict[str(x)+'.'+str(y-1)])
                else:
                    env.playerDict[str(x)+'.'+str(y-1)].point+=self.point
                    deletePlayer(self.coordinate.key)
            elif env.map[self.coordinate.x][self.coordinate.y-1] == 'A' or  env.map[self.coordinate.x][self.coordinate.y-1] == 'B' or  env.map[self.coordinate.x][self.coordinate.y-1] == 'T':
                pass
            else:
                self.coordinate.y -= 1
                
    def canEatPlayer(self, player):
        if not player.level == 3:
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
        self.type="pacman"
        self.point = 0
        self.level = level
        self.coordinate = coordinate       

    def move(self, direction):
        """
        Moves user in given direction by 1 road, a square.
        @param direction: string, Up | Down | Right | Left
        """
        if direction == "Right":
            if self.coordinate.x + 1 == 1000:
                pass
            elif env.map[self.coordinate.x+1][self.coordinate.y] == 'G':
                if self.canEatGhost(env.playerDict[str(x+1)+'.'+str(y)]):
                    self.point += env.playerDict[str(x+1)+'.'+str(y)].point 
                    deletePlayer(env.playerDict[str(x+1)+'.'+str(y)])
                else:
                    env.playerDict[str(x+1)+'.'+str(y)].point+=self.point
                    deletePlayer(self.coordinate.key)                      
                    
            elif env.map[self.coordinate.x+1][self.coordinate.y] == 'P':
                pass
            elif env.map[self.coordinate.x+1][self.coordinate.y] == 'A':
                if self.canEatForage(env.forageDict[str(x+1)+'.'+str(y)]):
                    self.point += env.forageDict[str(x+1)+'.'+str(y)].point 
                    env.deleteForage(env.forageDict[str(x+1)+'.'+str(y)])
                else:
                    pass
            elif env.map[self.coordinate.x+1][self.coordinate.y] == 'B':
                if self.canEatForage(env.forageDict[str(x+1)+'.'+str(y)]):
                    self.point += env.playerDict[str(x+1)+'.'+str(y)].point 
                    env.deleteForage(env.forageDict[str(x+1)+'.'+str(y)])
                else:
                    pass
            elif env.map[self.coordinate.x+1][self.coordinate.y] == 'T':
                if self.canEatForage(env.forageDict[str(x+1)+'.'+str(y)]):
                    self.point += env.playerDict[str(x+1)+'.'+str(y)].point 
                    env.deleteForage(env.forageDict[str(x+1)+'.'+str(y)])
                else:
                    pass
            else:
                self.coordinate.x += 1
            
        elif direction == "Down":
            if self.coordinate.y + 1 == 1000:
                pass
            elif env.map[self.coordinate.x][self.coordinate.y+1] == 'G':
                if self.canEatGhost(env.playerDict[str(x)+'.'+str(y+1)]):
                    self.point += env.playerDict[str(x)+'.'+str(y+1)].point 
                    deletePlayer(env.playerDict[str(x)+'.'+str(y+1)])
                else:
                    env.playerDict[str(x)+'.'+str(y+1)].point+=self.point
                    deletePlayer(self.coordinate.key)                      
                    
            elif env.map[self.coordinate.x][self.coordinate.y+1] == 'P':
                pass
            elif env.map[self.coordinate.x][self.coordinate.y+1] == 'A':
                if self.canEatForage(env.forageDict[str(x)+'.'+str(y+1)]):
                    self.point += env.forageDict[str(x)+'.'+str(y+1)].point 
                    env.deleteForage(env.forageDict[str(x)+'.'+str(y+1)])
                else:
                    pass
            elif env.map[self.coordinate.x][self.coordinate.y+1] == 'B':
                if self.canEatForage(env.forageDict[str(x)+'.'+str(y+1)]):
                    self.point += env.playerDict[str(x)+'.'+str(y+1)].point 
                    env.deleteForage(env.forageDict[str(x)+'.'+str(y+1)])
                else:
                    pass
            elif env.map[self.coordinate.x][self.coordinate.y+1] == 'T':
                if self.canEatForage(env.forageDict[str(x)+'.'+str(y+1)]):
                    self.point += env.playerDict[str(x)+'.'+str(y+1)].point 
                    env.deleteForage(env.forageDict[str(x)+'.'+str(y+1)])
                else:
                    pass
            else:
                self.coordinate.y += 1
       
       
       
       
       
       
        elif direction == "Left":
            if self.coordinate.x - 1 == -1:
                pass
            elif env.map[self.coordinate.x-1][self.coordinate.y] == 'G':
                if self.canEatGhost(env.playerDict[str(x-1)+'.'+str(y)]):
                    self.point += env.playerDict[str(x-1)+'.'+str(y)].point 
                    deletePlayer(env.playerDict[str(x-1)+'.'+str(y)])
                else:
                    env.playerDict[str(x-1)+'.'+str(y)].point+=self.point
                    deletePlayer(self.coordinate.key)                      
                    
            elif env.map[self.coordinate.x-1][self.coordinate.y] == 'P':
                pass
            elif env.map[self.coordinate.x-1][self.coordinate.y] == 'A':
                if self.canEatForage(env.forageDict[str(x-1)+'.'+str(y)]):
                    self.point += env.forageDict[str(x-1)+'.'+str(y)].point 
                    env.deleteForage(env.forageDict[str(x-1)+'.'+str(y)])
                else:
                    pass
            elif env.map[self.coordinate.x+1][self.coordinate.y] == 'B':
                if self.canEatForage(env.forageDict[str(x+1)+'.'+str(y)]):
                    self.point += env.playerDict[str(x+1)+'.'+str(y)].point 
                    env.deleteForage(env.forageDict[str(x+1)+'.'+str(y)])
                else:
                    pass
            elif env.map[self.coordinate.x-1][self.coordinate.y] == 'T':
                if self.canEatForage(env.forageDict[str(x-1)+'.'+str(y)]):
                    self.point += env.playerDict[str(x-1)+'.'+str(y)].point 
                    env.deleteForage(env.forageDict[str(x-1)+'.'+str(y)])
                else:
                    pass
            else:
                self.coordinate.x -= 1
       
       
       
       
        else:
            if self.coordinate.y - 1 == -1:
                pass
            elif env.map[self.coordinate.x][self.coordinate.y-1] == 'G':
                if self.canEatGhost(env.playerDict[str(x)+'.'+str(y-1)]):
                    self.point += env.playerDict[str(x)+'.'+str(y-1)].point 
                    deletePlayer(env.playerDict[str(x)+'.'+str(y-1)])
                else:
                    env.playerDict[str(x)+'.'+str(y-1)].point+=self.point
                    deletePlayer(self.coordinate.key)                      
                    
            elif env.map[self.coordinate.x][self.coordinate.y-1] == 'P':
                pass
            elif env.map[self.coordinate.x][self.coordinate.y-1] == 'A':
                if self.canEatForage(env.forageDict[str(x)+'.'+str(y-1)]):
                    self.point += env.forageDict[str(x)+'.'+str(y-1)].point 
                    env.deleteForage(env.forageDict[str(x)+'.'+str(y-1)])
                else:
                    pass
            elif env.map[self.coordinate.x][self.coordinate.y-1] == 'B':
                if self.canEatForage(env.forageDict[str(x)+'.'+str(y-1)]):
                    self.point += env.playerDict[str(x)+'.'+str(y-1)].point 
                    env.deleteForage(env.forageDict[str(x)+'.'+str(y-1)])
                else:
                    pass
            elif env.map[self.coordinate.x][self.coordinate.y-1] == 'T':
                if self.canEatForage(env.forageDict[str(x)+'.'+str(y-1)]):
                    self.point += env.playerDict[str(x)+'.'+str(y-1)].point 
                    env.deleteForage(env.forageDict[str(x)+'.'+str(y-1)])
                else:
                    pass
            else:
                self.coordinate.y -= 1
                
    
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
    def new(self,name, ptype, coordinate):  
        if ptype == "ghost":
            return Ghost(name,0,coordinate)
        else:
            return Pacman(name,0,1, coordinate)
    
