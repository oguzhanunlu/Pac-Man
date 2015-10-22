class Environment(object):
	"""Creates, saves, loads map"""
		
	playerList={}	
			
	def __init__(self):	
		"""Creates initial map with ways and forages.
		@return: Environment instance"""

	def save(self):	
		"""Saves current game state to file.
		@return: bool, True|False,whether it is saved successfully."""

	def load(self):
		"""Loads last saved game
		@return: bool, True|False, whether it is loaded succesfully."""
		
	def addRoad(self, road):
		"""Adds roads to given coordinate.
		@param road: Road
		@return: bool, True|False, whether road is added succesfully."""
	
	def deleteRoad(self, coordinate):
		"""Deletes roads.
		@param road: Road
		@param coordinate: Coordinate
		@return: bool, True|False, whether road is deleted succesfully."""
		
	def addForage(self, forage):
		"""Adds forage to  given coordinate.
		@param forage: Apple | Potato | Banana
		@return: bool, True|False, whether forage is added succesfully."""
		
	def deleteForage(self, coordinate):
		"""Deletes forage from  given coordinate.
		@param coordinate: Coordinate
		@return: bool, True|False, whether forage is deleted succesfully."""		
		
	def addPlayer(self, player):
		"""Adds player to  given coordinate.
		@param player: Player
		@return: bool, True|False, whether player is added succesfully."""
		
	def deletePlayer(self, player):
		"""Deletes player from  given coordinate.
		@param player: Player
		@return: bool, True|False, whether player is deleted succesfully."""
		
	def getScoreboard(self):
		"""Returns sorted player list.
		@return: dict, list of players with their point"""
		
    def showAllPlayers(self):
        """
        Prints all players.
        """
    
    def showAllForages(self):
        """
        Prints all forages.
        """
        
    def showAllRoads(self):
        """
        Prints all roads.
        """
