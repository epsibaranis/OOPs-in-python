# Accessing two numbers using OOPs Inheritance

from pgm272 import Atwono
class Child(Atwono):
    def __init__(self):
        Atwono.__init__(self,a=100,b=200)
    def S2no(self):
       a=self.getx()
       b=self.gety()
       c=a+b
       return c
    def Diffof2no(self):
       p=self.getx()
       q=self.gety()
       n=p-q
       return n
    def Productof2no(self):
       a=self.getx()
       b=self.gety()
       c=a*b
       return 
    def Divideof2no(self):
       a=self.getx()
       b=self.gety()
       c=a/b
       return c
    def Floorof2no(self):
       a=self.getx()
       b=self.gety()
       c=a//b
       return c
    def Biggestof2no(self):
       a=self.getx()
       b=self.gety()
       c=a if a>b  else b
       return c
    def Smallestof2no(self):
       a=self.getx()
       b=self.gety()
       c=a if a<b  else b
       return c
#main
a=Child()
a.setx(10)
a.sety(20)
z=a.S2no()
print(z)
a.setxy(40,20)
y=a.Diffof2no()
print(y)
a.setxy(40,20)
x=a.Divideof2no()
print(x)
a.setxy(100,50)
m=a.Productof2no()
print(m)
a.setxy(500,100)
n=a.Floorof2no()
print(n)
a.setxy(600,200)
q=a.Biggestof2no()
print(q)
a.setxy(400,700)
r=a.Biggestof2no()
print(r)