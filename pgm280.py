# Accessing two numbers using OOPs Inheritance
from pgm272 import Atwono
class point(Atwono):
    def __init__(self,a=0,b=0):
     Atwono.__init__(self,a,b)
#main
m=point()
m.setx(10)
m.sety(20)
a=m.getx()
print("get x value:",a)
b=m.gety()
print("get y value:",b)
m.setxy(100,200)
c=m.getxy()
print("get x, y value",c)