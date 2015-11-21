class Road(object):
    """
    Class definition of road.
    Each road is considered to be a square.
    """
    
    def __init__(self, coordinate):
        """
        Creates a road with given coordinate.
        @param coordinate: Coordinate
        @return: A road instance in given coordinate
        """
        self.coordinate=coordinate
