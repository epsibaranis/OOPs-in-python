# Accessing two numbers using OOPs Inheritance
from pgm272 import Atwono
class point(Atwono):
    def __init__(self,a=0,b=0):
     Atwono.__init__(self,a,b)
#main
m=point()
m.print()
m.setx(10)
m.print()
m.sety(20)
m.print()
a=m.getx()
print(a)
b=m.gety()
print(b)
m.setxy(100,200)
m.print()
c=m.getxy()
print(c)