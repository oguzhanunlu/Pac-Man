#TODO load-save 

class Environment(object):
    """Creates, saves, loads map"""
	
		
    def __init__(self):	
        """Creates initial map with ways and forages.
        @return: Environment instance"""
        self.playerDict = {}
        self.forageDict = {}
        self.roadDict = {}
        self.map = [['X','X','X','X'],['X','X','X','X'],['X','X','X','X'],['X','X','X','X']]


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
	    
	    self.roadDict[road.coordinate.key]=road
	    self.map[road.coordinate.x][road.coordinate.y] = 'r' #this is only needed for phase 1 testing
    
    def addForage(self, forage):
        """Adds forage to  given coordinate.
        @param forage: Apple | Tomato | Banana
        @return: bool, True|False, whether forage is added succesfully."""
        self.forageDict[forage.coordinate.key]=forage
        self.map[forage.coordinate.x][road.coordinate.y]=forage.kind[0]


	        
    def deleteForage(self, forage):
	    """Deletes forage from  given coordinate.
	    @param coordinate: Coordinate
	    @return: bool, True|False, whether forage is deleted succesfully."""		
	    del self.forageDict[forage.coordinate.key]
	    self.map[forage.coordinate.x][road.coordinate.y]='r'
	    
    def addPlayer(self, player):
	    """Adds player to  given coordinate.
	    @param player: Player
	    @return: bool, True|False, whether player is added succesfully."""
	    self.playerDict[player.coordinate.key]=player
	    self.map[player.coordinate.x][player.coordinate.y]=player.type[0]
	    
    def deletePlayer(self, player):
	    """Deletes player from  given coordinate.
	    @param player: Player
	    @return: bool, True|False, whether player is deleted succesfully."""
	    del self.playerDict[player.coordinate.key]
	    self.map[player.coordinate.x][player.coordinate.y]='r'
	    
    def getScoreboard(self):
        """Returns sorted player list.
        @return: dict, list of players with their point"""

        s=sorted(playerDict.items(),key=operator.attrgetter("point")) 
        playerNameList = []
        playerPointList = []
        for i in s:
            playerNameList.append(i.name)
            playerPointList.append(i.point)

        list1 = list(reversed(playerNameList))
        list2 = list(reversed(playerPointList))

        for p in xrange(len(list1)):
            print list1[p], list2[p] 

        return [list1,list2]	
    
        
    def getMap(self, player, width, height):
        """
        Returns all players.
        """
        x1 = player.coordinate.x - width
        x2 = player.coordinate.x + width
        y1 = player.coordinate.y - height
        y2 = player.coordinate.x + height
        
        if x1 <= 0:
            x1 = 0
        if x2 > 999:
            x2 = 999
        if y1 > 0:
            y1 = 0
        if y2 > 999:
            y2 = 999
        
        for i in xrange(x1,x2):
            for j in xrange(y1,y2):
                print self.map[i][j],
            print   
        
'''        
    def getAllForages(self, player, width, height):
        """
        Returns all forages.
        """
        
    def getAllRoads(self, player, width, height):
        """
        Returns all roads.
        """
'''
