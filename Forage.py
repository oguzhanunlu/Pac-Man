class Forage(object):
    """
    The object players try to eat on map.
    Apple: 1 point, Beginner & Intermediate & Pro players can eat
    Banana 25 points, Only Intermediate & Pro players can eat
    Potato 50 points, Only Pro players eat
    """
    
    def __init__(self, kind):
        """
        Creates a forage with given kind.
        @param kind: string, Apple | Banana | Potato 
        @return: A forage instance of given kind
        """
        
        self.kind = kind
