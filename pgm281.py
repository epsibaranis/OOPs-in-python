# Accessing two numbers using OOPs Inheritance
from pgm277 import Atwono
class point(Atwono):
     def __init__(self,o=10,i=60,):
        Atwono.__init__(self,o,i)
     def add(self,b):
        c=point()
        c._x=self._x+b._x
        c._y=self._y+b._y
        return c
     def diff(self,b):
        c=point()
        c._x=self._x-b._x
        c._y=self._y-b._y
        return c
     def multiply(self,b):
        c=point()
        c._x=self._x*b._x
        c._y=self._y*b._y
        return c 
a=point()
b=point()
c=a.add(b)
c.print()
a.setxy(50,200)
d=a.diff(b)
d.print()
a.setxy(20,10)
b.setxy(10,50)
s=a.multiply(b)
s.print()     