class Player(object):
    """
    Class definition of Player
    Beginner Player     :A player with point below 5
    Intermediate Player :A player with point between 5 and 35
    Pro Player          :A player with point above 35  
    """
    
    score = 0
    
    def __init__(self, level, coordinate):
        """
        @param level: string, Beginner | Intermediate | Pro
        @param coordinate: Coordinate
        @return : A player instance 
        """
    
    def kill(self):
        """
        Set score to 0.
        """     
        
    def move(self, direction):
        """
        Moves user in given direction by 1 road, a square.
        @param direction: string, Up | Down | Right | Left
        """
    
