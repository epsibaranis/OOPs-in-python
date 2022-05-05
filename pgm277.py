# Accessing two numbers using OOPs Inheritance

class Atwono():
    _x=None
    _y=None
    def __init__(self,a=0,b=0):
       self._x=a
       self._y=b
    def setx(self,a=0):
       self._x=a    
    def sety(self,b=0):
       self._y=b
    def setxy(self,a=0,b=0):
       self._x=a
       self._y=b
    def resetxy(self,a=0,b=0):
       self._x=a
       self._y=b
    def getx(self):
        return (self._x)
    def gety(self):
        return (self._y)
    def getxy(self):
        return (self._x,self._y)
    def print(self):
        print(self._x,self._y)
#main
