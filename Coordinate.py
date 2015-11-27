class Coordinate(object):
    """
    Class definition of coordinate.
    """
    
    def __init__(self, x, y):
        """
        @param x: x-coordinate
        @param y: y-coordinate
        @return: A coordinate instance with given values
        """
        self.x=x
        self.y=y
        self.key=str(x)+'.'+str(y)
