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
print("Sum of  two numbers:",z)
d=a.Diffof2no()
print("Difference of two numbers:",d)
b=a.Productof2no()
print("product of two numbers:",b)
m=a.Divideof2no()
print("Division of two numbers:",m)
n=a.Floorof2no()
print("Floor of two numbers",n)
q=a.Biggestof2no()
print("Biggest of two numbers:",q)
r=a.Smallestof2no()
print("Smallest of two numbers:",r)   