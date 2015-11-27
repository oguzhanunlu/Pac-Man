class Forage(object):
 '''
    """
    The object players try to eat on map.
    Apple: 1 point, Beginner & Intermediate & Pro players can eat
    Banana 25 points, Only Intermediate & Pro players can eat
    Tomato 50 points, Only Pro players eat
    """
    
    def __init__(self, kind):
        """
        Creates a forage with given kind.
        @param kind: string, Apple | Banana | Tomato 
        @return: A forage instance of given kind
        """
        
        self.kind = kind
        '''
        
class Apple(Forage):        

	def __init__(self,coordinate):
		self.kind="Apple"	
		self.point=1
		self.coordinate=coordinate

class Banana(Forage):        

	def __init__(self,coordinate):
		self.kind="Banana"
		self.point=25
		self.coordinate=coordinate

class Tomato(Forage):        

	def __init__(self,coordinate):
		self.kind="Tomato"
		self.point=50
		self.coordinate=coordinate
				
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
class ForageFactory(object):
    """
    Factory design pattern to specify type of players.
    """
    def new(self, name, coordinate):  
        if name == "apple":
            return Apple( coordinate)
        elif name == "banana":
        	return Banana(coordinate)
        else:
            return Tomato(coordinate)
