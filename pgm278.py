#Accessing two numbers using OOPs Inheritance
from pgm277 import Atwono
class child(Atwono):
      def __init__(self,a=10,b=20):
          Atwono.__init__(self,a,b)
      def sumoftwono(self):
          c=self._x+self._y
          return c
      def productoftwono(self):
          c=self._x*self._y
          return c
      def divideoftwono(self):
          c=self._x/self._y
          return c
      def flooroftwono(self):
          c=self._x//self._y
          return c
      def Biggestoftwono(self):
          c=self._x if self._x>self._y else self._y
          return c
      def smallestoftwono(self):
          c=self._x if self._x<self._y else self._y
          return c