# Accessing two numbers using OOPs Inheritance
from pgm277 import Atwono
class Athreeno(Atwono):
    _z=None
    def __init__(self,a=0,b=0,c=0):
        Atwono.__init__(self,a,b)
    def setz(self,c=0):
        self._z=c
    def setxyz(self,a=0,b=0,c=0):
        Atwono.setxy(self,a,b)
        self._z=c
    def resetxy(self,a=0,b=0,c=0):
        self._x=a
        self._y=b
        self._z=c
    def getz(self):
        return(self._z)
    def getxyz(self):
        return(self._z)
        return(self._x)
        return(self._y)
    