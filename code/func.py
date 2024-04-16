import numpy
import math

class Vector:
    __s = 4
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return("({}, {})".format(self.x, self.y))
    def length(self):
        return ((self.x)**2 + (self.y)**2)**0.5
    def angle(self):
        return math.atan(self.y/self.x)
    def summ_vect(self, vector1):
        return Vector(self.x + vector1.x, self.y + vector1.y)
    def m_vect(self, vector1):
        return Vector(self.x - vector1.x, self.y - vector1.y)
    def pr_scal(self, vector1):
        return self.x * vector1.x + self.y * vector1.y
