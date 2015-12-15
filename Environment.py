#TODO load-save 
import random
import operator
import pickle
from Coordinate import *
from Player import *
from Forage import *
from Road import *
from threading import *

lock=Lock()
locked = [[True for i in xrange(40)] for i in xrange(40)]
cond = Condition(lock)



class Environment(object):
    """Creates, saves, loads map"""
    
        
    def __init__(self):
        """Creates initial map with ways and forages.
        @return: Environment instance"""
        self.playerDict = {}
        self.forageDict = {}
        self.roadDict = {}
        #self.map = [['X','X','X','X'],['X','X','X','X'],['X','X','X','X'],['X','X','X','X']]
        self.map = [["X" for i in xrange(40)] for i in xrange(40)]
        self.usernames = []
        
    def getlock(self,c1,c2):

        global lock
        global locked
        global cond
        lock.acquire()
        print 'getlock: ',c1.x, c1.y,c2.x,c2.y
        while 1:
            if locked[c1.x][c1.y]==True and locked[c2.x][c2.y]==True:
                locked[c1.x][c1.y]=False
                locked[c2.x][c2.y]=False
                lock.release()
                return
            else:
                print "I'm blocked at ",c1.x,c1.y,c2.x,c2.y
                cond.wait()
             


    def freelock(self,c1,c2):

        global lock
        global locked
        global cond
        lock.acquire()
        print 'freelock: ',c1.x, c1.y,c2.x,c2.y
        locked[c1.x][c1.y]=True
        locked[c2.x][c2.y]=True
        cond.notifyAll()
        lock.release()
    def save(self):
        """Saves current game state to file.
        @return: bool, True|False,whether it is saved successfully."""
        
        with open("player","wb") as f:
            pickle.dump(self.playerDict, f)
        with open("forage","wb") as f:
            pickle.dump(self.forageDict, f)
        with open("road","wb") as f:
              pickle.dump(self.roadDict, f)
        with open("map","wb") as f:
            pickle.dump(self.map, f)
        

    def load(self):
        """Loads last saved game
        @return: bool, True|False, whether it is loaded succesfully."""

        with open("player","rb") as f:
            self.playerDict = pickle.load(f)
        with open("forage","rb") as f:
            self.forageDict = pickle.load(f)
        with open("road","rb") as f:
            self.roadDict = pickle.load(f)
        with open("map","rb") as f:
            self.map = pickle.load(f)

    
    def addRoad(self, road):
        """Adds roads to given coordinate.
        @param road: Road
        @return: bool, True|False, whether road is added succesfully."""
        
        self.roadDict[road.coordinate.key]=road
        self.map[road.coordinate.x][road.coordinate.y] = 'r'#this is only needed for phase 1 testing
    
    def addForage(self, forage):
        """Adds forage to  given coordinate.
        @param forage: Apple | Tomato | Banana
        @return: bool, True|False, whether forage is added succesfully."""
        if  self.map[forage.coordinate.x][forage.coordinate.y]=='r':
            self.forageDict[forage.coordinate.key]=forage
            self.map[forage.coordinate.x][forage.coordinate.y]=forage.kind[0]       
            
    def deleteForage(self, forage):
        """Deletes forage from  given coordinate.
        @param coordinate: Coordinate
        @return: bool, True|False, whether forage is deleted succesfully."""        
        del self.forageDict[forage.coordinate.key]
        self.map[forage.coordinate.x][forage.coordinate.y]='r'
        
    def addPlayer(self, player):
        """Adds player to  given coordinate.
        @param player: Player
        @return: bool, True|False, whether player is added succesfully."""
        if  self.map[player.coordinate.x][player.coordinate.y]=='r':
            self.playerDict[player.coordinate.key]=player
            self.map[player.coordinate.x][player.coordinate.y]=player.type[0]
            self.usernames.append(player.name)
        
    def deletePlayer(self, player):
        """Deletes player from  given coordinate.
        @param player: Player
        @return: bool, True|False, whether player is deleted succesfully."""
        del self.playerDict[player.coordinate.key]
        self.map[player.coordinate.x][player.coordinate.y]='r'
        del player
    
    def mapGenerator(self):
        for i in range(0,40,10):
            self.map[i] = ['r']*40
            #print self.map[i]
        for i in range(0,40,10):
            for j in range(0,40):
                self.map[j][i] = 'r'                    
                self.map[39] = ['r']*40
            for j in range(0,40):
                self.map[j][39] = 'r'
    def sendPlayerRandom(self, player):
        i = random.randrange(0,4)
        i *= 10
        for j in range(0,40):
            if self.map[i][j] == "r":
                player.coordinate.x = i
                player.coordinate.y = j
                player.coordinate.key=str(i)+'.'+str(j)
                self.playerDict[player.coordinate.key]=player
                self.map[i][j] = player.type[0]
                break
        
    def getScoreBoard(self):
        """Returns sorted player list.
        @return: dict, list of players with their point"""

        s=sorted(self.playerDict.values(),key=operator.attrgetter("point"))
        playerNameList = []
        playerPointList = []
        for i in s:
            playerNameList.append(i.name)
            playerPointList.append(i.point)

        list1 = list(reversed(playerNameList))
        list2 = list(reversed(playerPointList))


        return [list1,list2]
    
    def printDict(self, d):
        for i in d:
            print i, d[i].type
    
    def getAllMap(self):
    
        for i in range(0,40):
            for j in range(0,40):
                print self.map[i][j],
            print
   
    def getMap(self, player, width, height):
        """
        Returns all players."""
        x1 = player.coordinate.x - width
        x2 = player.coordinate.x + width
        y1 = player.coordinate.y - height
        y2 = player.coordinate.y + height
        bufx=0
        tufx=0
        bufy=0
        tufy=0
        if x1 <= 0:
            bufx=x1
            tufx=-bufx
            x1 = 0
        elif x2 > 39:
            bufx=x2-39
            x2 = 39
        if y1 <= 0:
            bufy=y1
            tufy=-bufy
            y1 = 0
        elif y2 > 39:
            bufy=y2-39
            y2 = 39
        
        
        #print bufx,bufy,tufx,tufy
        for i,k in zip(range(x1,x2+1),range(2*width+1-abs(bufx))):
            for j,l in zip(range(y1,y2+1),range(2*height+1-abs(bufy))):
                player.frame[k+tufx][l+tufy] = self.map[i][j]
        return player.frame
        
        
    def move(self, player, direction):
        if player.type == "Ghost":
            if direction == "d":
                
                if player.coordinate.x + 1 < 40:
                
                    next = Coordinate(player.coordinate.x+1,player.coordinate.y)
                    current = Coordinate(player.coordinate.x,player.coordinate.y)
                    self.getlock(player.coordinate,next)
                   
                    if self.map[player.coordinate.x+1][player.coordinate.y] == 'G' or self.map[player.coordinate.x+1][player.coordinate.y] == 'X':
                        self.freelock(current,next)    
                        return
                    elif self.map[player.coordinate.x+1][player.coordinate.y] == 'P':
                        if player.canEatPlayer(self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)]):
                            player.point += self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)].point 
                            self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)].point /= 2
                            if self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)].point < 5:
                                self.deletePlayer(self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)])
                            else:
                                self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)].levelChanger()
                                self.sendPlayerRandom(self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)])
                            player.coordinate.x += 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = 'G'
                            self.map[player.coordinate.x-1][player.coordinate.y] = 'r'
                        else:
                            self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)].point+=player.point
                            self.map[player.coordinate.x][player.coordinate.y] = 'r'
                            self.deletePlayer(player)
                    elif self.map[player.coordinate.x+1][player.coordinate.y] == 'A' or  self.map[player.coordinate.x+1][player.coordinate.y] == 'B' or  self.map[player.coordinate.x+1][player.coordinate.y] == 'T':
                        player.coordinate.x += 1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        del self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)]
                        self.map[player.coordinate.x][player.coordinate.y] = 'G'
                        self.map[player.coordinate.x-1][player.coordinate.y] = 'r'
                        del self.forageDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)]
                    else:
                        del self.playerDict[player.coordinate.key]
                        player.coordinate.x += 1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        self.map[player.coordinate.x][player.coordinate.y] = 'G'
                        self.map[player.coordinate.x-1][player.coordinate.y] = 'r'
                    self.freelock(current,next)    
                else:
                    return
            elif direction == "r":
                if player.coordinate.y + 1 < 40:
                    next = Coordinate(player.coordinate.x,player.coordinate.y+1)
                    current = Coordinate(player.coordinate.x,player.coordinate.y)
                    self.getlock(player.coordinate,next)

                    if self.map[player.coordinate.x][player.coordinate.y+1] == 'G' or self.map[player.coordinate.x][player.coordinate.y+1] == 'X':
                        self.freelock(current,next)
                        return
                    elif self.map[player.coordinate.x][player.coordinate.y+1] == 'P':
                        if player.canEatPlayer(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)]):
                            player.point += self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)].point
                            self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)].point /= 2
                            if self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)].point < 5:
                                self.deletePlayer(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)])
                            else:
                                self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)].levelChanger()
                                self.sendPlayerRandom(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)])
                            player.coordinate.y += 1 
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = 'G'
                            self.map[player.coordinate.x][player.coordinate.y-1] = 'r'
                        else:
                            self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)].point+=player.point
                            self.map[player.coordinate.x][player.coordinate.y] = 'r'
                            self.deletePlayer(player)
                    elif self.map[player.coordinate.x][player.coordinate.y+1] == 'A' or  self.map[player.coordinate.x][player.coordinate.y+1] == 'B' or  self.map[player.coordinate.x][player.coordinate.y+1] == 'T':
                        player.coordinate.y += 1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        del self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)]
                        self.map[player.coordinate.x][player.coordinate.y] = 'G'
                        self.map[player.coordinate.x][player.coordinate.y-1] = 'r'
                        del self.forageDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)]
                    else:
                        del self.playerDict[player.coordinate.key]
                        player.coordinate.y += 1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        self.map[player.coordinate.x][player.coordinate.y] = 'G'
                        self.map[player.coordinate.x][player.coordinate.y-1] = 'r'
                    self.freelock(current,next)
                else:
                    return
            elif direction == "u":
                if player.coordinate.x - 1 >= 0:
                    next = Coordinate(player.coordinate.x-1,player.coordinate.y)
                    current = Coordinate(player.coordinate.x,player.coordinate.y)
                    self.getlock(player.coordinate,next)
       
                    if self.map[player.coordinate.x-1][player.coordinate.y] == 'G' or self.map[player.coordinate.x-1][player.coordinate.y] == 'X':
                        self.freelock(current,next)
                        return
                    elif self.map[player.coordinate.x-1][player.coordinate.y] == 'P':
                       
                        if player.canEatPlayer(self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)]):
                            player.point += self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)].point 
                            self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)].point /= 2
                            if self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)].point < 5:
                                self.deletePlayer(self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)])
                            else:
                                self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)].levelChanger()
                                self.sendPlayerRandom(self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)])
                            player.coordinate.x -= 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = 'G'
                            self.map[player.coordinate.x+1][player.coordinate.y] = 'r'
                        else :
                            self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)].point+=player.point
                            self.map[player.coordinate.x][player.coordinate.y] = 'r'
                            self.deletePlayer(player)
                    elif self.map[player.coordinate.x-1][player.coordinate.y] == 'A' or  self.map[player.coordinate.x-1][player.coordinate.y] == 'B' or  self.map[player.coordinate.x-1][player.coordinate.y] == 'T':
                        player.coordinate.x -= 1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        del self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)]
                        self.map[player.coordinate.x][player.coordinate.y] = 'G'
                        self.map[player.coordinate.x+1][player.coordinate.y] = 'r'
                        del self.forageDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)]


                    else:
                        del self.playerDict[player.coordinate.key]
                        player.coordinate.x -= 1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        self.map[player.coordinate.x][player.coordinate.y] = 'G'
                        self.map[player.coordinate.x+1][player.coordinate.y] = 'r'
                    self.freelock(current,next)
                else:
                    return
            else:
                if player.coordinate.y - 1 > -1:

                    next = Coordinate(player.coordinate.x,player.coordinate.y-1)
                    current = Coordinate(player.coordinate.x,player.coordinate.y)
                    self.getlock(player.coordinate,next)
       
                    if self.map[player.coordinate.x][player.coordinate.y-1] == 'G' or self.map[player.coordinate.x][player.coordinate.y-1] == 'X':
                        self.freelock(current,next)
                        return
                    elif self.map[player.coordinate.x][player.coordinate.y-1] == 'P':
                        if player.canEatPlayer(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)]):
                           
                            player.point += self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)].point
                            self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)].point /= 2
                            if self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)].point < 5:
                               
                                self.deletePlayer(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)])
                            else:
                                self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)].levelChanger()
                                self.sendPlayerRandom(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)])
                            player.coordinate.y -= 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            del self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)]
                            self.map[player.coordinate.x][player.coordinate.y] = 'G'
                            self.map[player.coordinate.x][player.coordinate.y+1] = 'r'
                        else:
                            self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)].point+=player.point
                            self.map[player.coordinate.x][player.coordinate.y] = 'r'
                            self.deletePlayer(player)
                    elif self.map[player.coordinate.x][player.coordinate.y-1] == 'A' or  self.map[player.coordinate.x][player.coordinate.y-1] == 'B' or  self.map[player.coordinate.x][player.coordinate.y-1] == 'T':
                        player.coordinate.y -=1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        del self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)]
                        self.map[player.coordinate.x][player.coordinate.y] = 'G'
                        self.map[player.coordinate.x][player.coordinate.y+1] = 'r'
                        del self.forageDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)]

                    else:
                        del self.playerDict[player.coordinate.key]
                        player.coordinate.y -= 1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        self.map[player.coordinate.x][player.coordinate.y] = 'G'
                        self.map[player.coordinate.x][player.coordinate.y+1] = 'r'
                    self.freelock(current,next)    
                else:
                    return
        elif player.type == "Pacman":
            if direction == "d":
                if player.coordinate.x + 1 < 40:
                    next = Coordinate(player.coordinate.x+1,player.coordinate.y)
                    current = Coordinate(player.coordinate.x,player.coordinate.y)
                    self.getlock(player.coordinate,next)
                        
                    if self.map[player.coordinate.x+1][player.coordinate.y] == 'P': 
                        self.freelock(current,next)
                        return
                    elif self.map[player.coordinate.x+1][player.coordinate.y] == 'X':
                        if player.level == 3:
                            del self.playerDict[player.coordinate.key]
                            player.coordinate.x += 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = "P"
                            self.map[player.coordinate.x-1][player.coordinate.y] = "r" 
                    elif self.map[player.coordinate.x+1][player.coordinate.y] == 'G':
                        if player.canEatGhost(self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)]):
                            player.point += self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)].point 
                            self.deletePlayer(self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)])
                            player.coordinate.x += 1 
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = 'P'
                            self.map[player.coordinate.x-1][player.coordinate.y] = 'r'
                        else:
                            self.playerDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)].point+=player.point
                            player.point /= 2
                            if player.point < 5:
                                self.deletePlayer(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)])
                                self.map[player.coordinate.x][player.coordinate.y]='r'
                            else:
                                self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)].levelChanger()
                                self.map[player.coordinate.x][player.coordinate.y] = 'r'
                                self.sendPlayerRandom(player)
                            # ghost pacmani yedi, pacmani random bir yere tasi
                            
                    elif self.map[player.coordinate.x+1][player.coordinate.y] == 'P':
                        self.freelock(current,next)
                        return
                    elif self.map[player.coordinate.x+1][player.coordinate.y] == 'A' or self.map[player.coordinate.x+1][player.coordinate.y] == 'B' or self.map[player.coordinate.x+1][player.coordinate.y] == 'T':
                        if player.canEatForage(self.forageDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)]):
                            player.point += self.forageDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)].point 
                            self.deleteForage(self.forageDict[str(player.coordinate.x+1)+'.'+str(player.coordinate.y)])
                            del self.playerDict[player.coordinate.key]
                            player.coordinate.x += 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = 'P'
                            self.map[player.coordinate.x-1][player.coordinate.y] = 'r'
                        else:
                            self.freelock(current,next)
                            return

                    else:
                        del self.playerDict[player.coordinate.key]
                        player.coordinate.x += 1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        self.map[player.coordinate.x][player.coordinate.y] = 'P'
                        self.map[player.coordinate.x-1][player.coordinate.y] = 'r'
                    self.freelock(current,next)
                else:
                    return                   
            elif direction == "r":
                if player.coordinate.y + 1 < 40:
                    next = Coordinate(player.coordinate.x,player.coordinate.y+1)
                    current = Coordinate(player.coordinate.x,player.coordinate.y)
                    self.getlock(player.coordinate,next)

                    if self.map[player.coordinate.x][player.coordinate.y+1] == 'P': 
                        self.freelock(current,next)
                        return
                    elif self.map[player.coordinate.x][player.coordinate.y+1] == 'X':
                        if player.level == 3:
                            del self.playerDict[player.coordinate.key]
                            player.coordinate.y += 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = "P"
                            self.map[player.coordinate.x][player.coordinate.y-1] = "r"
                    elif self.map[player.coordinate.x][player.coordinate.y+1] == 'G':
                        if player.canEatGhost(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)]):
                            player.point += self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)].point 
                            self.deletePlayer(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)])
                            player.coordinate.y += 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = 'P'
                            self.map[player.coordinate.x][player.coordinate.y-1] = 'r'
                        else:
                            self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)].point+=player.point
                            player.point /= 2
                            if player.point < 5:
                                self.deletePlayer(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)])
                                self.map[player.coordinate.x][player.coordinate.y]='r'
                            else:
                                self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)].levelChanger()
                                self.map[player.coordinate.x][player.coordinate.y] = 'r'
                                self.sendPlayerRandom(player)
                           
                    elif self.map[player.coordinate.x][player.coordinate.y+1] == 'P':
                        self.freelock(current,next)
                        return
                    elif self.map[player.coordinate.x][player.coordinate.y+1] == 'A' or self.map[player.coordinate.x][player.coordinate.y+1] == 'B' or self.map[player.coordinate.x][player.coordinate.y+1] == 'T':
                        if player.canEatForage(self.forageDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)]):
                            player.point += self.forageDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)].point 
                            self.deleteForage(self.forageDict[str(player.coordinate.x)+'.'+str(player.coordinate.y+1)])
                            del self.playerDict[player.coordinate.key]
                            player.coordinate.y += 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = 'P'
                            self.map[player.coordinate.x][player.coordinate.y-1] = 'r'
                        else:
                            self.freelock(current,next)
                            return

                    else:
                        del self.playerDict[player.coordinate.key]
                        player.coordinate.y += 1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        self.map[player.coordinate.x][player.coordinate.y] = 'P'
                        self.map[player.coordinate.x][player.coordinate.y-1] = 'r'
                    self.freelock(current,next)         
                else:
                    return
            elif direction == "u":
                if player.coordinate.x - 1 > -1:
                    next = Coordinate(player.coordinate.x-1,player.coordinate.y)
                    current = Coordinate(player.coordinate.x,player.coordinate.y)
                    self.getlock(player.coordinate,next)

                    if self.map[player.coordinate.x-1][player.coordinate.y] == 'P': 
                        self.freelock(current,next)
                        return
                    elif self.map[player.coordinate.x-1][player.coordinate.y] == 'X':
                        if player.level == 3:
                            del self.playerDict[player.coordinate.key]
                            player.coordinate.x -= 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = "P"
                            self.map[player.coordinate.x+1][player.coordinate.y] = "r"
                    elif self.map[player.coordinate.x-1][player.coordinate.y] == 'G':
                       
                        if player.canEatGhost(self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)]):
                           
                            player.point += self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)].point 
                            self.deletePlayer(self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)])
                            player.coordinate.x -= 1 
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = 'P'
                            self.map[player.coordinate.x+1][player.coordinate.y] = 'r'
                        else:
                            self.playerDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)].point+=player.point
                            player.point /= 2
                            if player.point < 5:
                                self.deletePlayer(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)])
                                self.map[player.coordinate.x][player.coordinate.y]='r'
                            else:
                                self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)].levelChanger()
                                self.map[player.coordinate.x][player.coordinate.y] = 'r'
                                self.sendPlayerRandom(player)
                           
                    elif self.map[player.coordinate.x-1][player.coordinate.y] == 'P':
                        self.freelock(current,next)
                        return
                    elif self.map[player.coordinate.x-1][player.coordinate.y] == 'A' or self.map[player.coordinate.x-1][player.coordinate.y] == 'B' or self.map[player.coordinate.x-1][player.coordinate.y] == 'T':
                        if player.canEatForage(self.forageDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)]):
                            player.point += self.forageDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)].point 
                            self.deleteForage(self.forageDict[str(player.coordinate.x-1)+'.'+str(player.coordinate.y)])
                            del self.playerDict[player.coordinate.key]
                            player.coordinate.x -= 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = 'P'
                            self.map[player.coordinate.x+1][player.coordinate.y] = 'r'
                        else:
                            self.freelock(current,next)
                            return

                    else:
                        del self.playerDict[player.coordinate.key]
                        player.coordinate.x -= 1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        self.map[player.coordinate.x][player.coordinate.y] = 'P'
                        self.map[player.coordinate.x+1][player.coordinate.y] = 'r'
                    self.freelock(current,next)    
                else:
                    return           
            else:
                if player.coordinate.y - 1 > -1:
                    next = Coordinate(player.coordinate.x,player.coordinate.y-1)
                    current = Coordinate(player.coordinate.x,player.coordinate.y)
                    self.getlock(player.coordinate,next)
       
                    if self.map[player.coordinate.x][player.coordinate.y-1] == 'P': 
                        self.freelock(current,next)
                        return
                    elif self.map[player.coordinate.x][player.coordinate.y-1] == 'X':
                        if player.level == 3:
                            del self.playerDict[player.coordinate.key]
                            player.coordinate.y -= 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = "P"
                            self.map[player.coordinate.x][player.coordinate.y+1] = "r"
                    elif self.map[player.coordinate.x][player.coordinate.y-1] == 'G':
                        if player.canEatGhost(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)]):
                            player.point += self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)].point 
                            self.deletePlayer(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)])
                            player.coordinate.y -= 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y) 
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = 'P'
                            self.map[player.coordinate.x][player.coordinate.y+1] = 'r'
                        else:
                            self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)].point+=player.point
                            player.point /= 2
                            if player.point < 5:
                                self.deletePlayer(self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)])
                                self.map[player.coordinate.x][player.coordinate.y]='r'
                            else:
                                self.playerDict[str(player.coordinate.x)+'.'+str(player.coordinate.y)].levelChanger()
                                self.map[player.coordinate.x][player.coordinate.y] = 'r'
                                self.sendPlayerRandom(player)
                           
                    elif self.map[player.coordinate.x][player.coordinate.y-1] == 'P':
                        self.freelock(current,next)
                        return
                    elif self.map[player.coordinate.x][player.coordinate.y-1] == 'A' or self.map[player.coordinate.x][player.coordinate.y-1] == 'B' or self.map[player.coordinate.x][player.coordinate.y-1] == 'T':
                        if player.canEatForage(self.forageDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)]):
                            player.point += self.forageDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)].point 
                            self.deleteForage(self.forageDict[str(player.coordinate.x)+'.'+str(player.coordinate.y-1)])
                            del self.playerDict[player.coordinate.key]
                            player.coordinate.y -= 1
                            player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                            self.playerDict[player.coordinate.key] = player
                            self.map[player.coordinate.x][player.coordinate.y] = 'P'
                            self.map[player.coordinate.x][player.coordinate.y+1] = 'r'
                        else:
                            self.freelock(current,next)
                            return


                    else:
                        del self.playerDict[player.coordinate.key]
                        player.coordinate.y -= 1
                        player.coordinate.key=str(player.coordinate.x)+'.'+str(player.coordinate.y)
                        self.playerDict[player.coordinate.key] = player
                        self.map[player.coordinate.x][player.coordinate.y] = 'P'
                        self.map[player.coordinate.x][player.coordinate.y+1] = 'r'
                    self.freelock(current,next)
                else:
                   return  
            player.levelChanger()
