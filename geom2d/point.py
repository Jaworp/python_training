from math import sqrt
class Point:
    def __init__(self, x, y):  #konstruktor __init__
        self.x = x
        self.y = y

    def distance(self,p2):  #metoda
        dx= p2.x - self.x
        dy= p2.y - self.y
        return sqrt(dx*dx + dy*dy)

    def __eq__(self, other):    # operacja porównanie
        return self.x == other.y and self.y ==other.y