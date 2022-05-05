# Accessing two numbers using OOPs Inheritance

from pgm272 import Atwono
class Child(Atwono):
    def __init__(self,a=100,b=200):
        Atwono.__init__(self,a,b)
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
       return c
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
z=a.S2no()
a.printf()
print(z)
d=a.Diffof2no()
print(d)
b=a.Productof2no()
print(b)
m=a.Divideof2no()
print(m)
n=a.Floorof2no()
print(n)
q=a.Biggestof2no()
print(q)
r=a.Smallestof2no()
print(r)

    