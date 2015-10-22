class Environment(object):
	"""Creates, saves, loads map"""
		
	playerList={}	
			
	def __init__(self):	
		"""Creates initial map with ways and forages.
		@return: Environment instance"""

	def save(self):	
		"""Saves current game state to file.
		@return: bool, True|False,whether it is saved successfully."""

	def	load(self):
		"""Loads last saved game
		@return: bool, True|False, whether it is loaded succesfully."""
		
	def addRoad(self, road, coordinate):
		"""Adds roads to given coordinate.
		@return: bool, True|False, whether road is added succesfully."""
	
	def deleteRoad(self, road, coordinate):
		"""Deletes roads from given coordinate.
		@return: bool, True|False, whether road is deleted succesfully."""
		
	def addForage(self, forage, coordinate):
		"""Adds forage to  given coordinate.
		@return: bool, True|False, whether forage is added succesfully."""
		
	def deleteForage(self, forage, coordinate):
		"""Deletes forage from  given coordinate.
		@return: bool, True|False, whether forage is deleted succesfully."""		
		
	def addPlayer(self, player, coordinate):
		"""Adds player to  given coordinate.
		@return: bool, True|False, whether player is added succesfully."""
		
	def deletePlayer(self, player, coordinate):
		"""Deletes player from  given coordinate.
		@return: bool, True|False, whether player is deleted succesfully."""
		
	def getScoreboard(self):
		"""Returns rated player list.
		@return: dict, list of players with their point"""
