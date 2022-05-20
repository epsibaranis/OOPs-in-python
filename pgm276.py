# Operate three numbers  using OOPs Inheritance
from pgm275 import Athreeno
class Operatethreeno(Athreeno):
   def __init__(self,a=100,b=200,c=300):
        Athreeno.__init__(self,a,b,c)
   def sumofthreeno(self):
       a=self.getx()
       b=self.gety()
       c=self.getz()
       d=a+b+c
       return d
   def Productofthreeno(self):
       a=self.getx()
       b=self.gety()
       c=self.getz()
       d=a*b*c
       return d
   def Biggestofthreeno(self):
       a=self.getx()
       b=self.gety()
       c=self.getz()
       d=(a if a>c else c)if a>b else (b if b>c else c)
       return d
   def Smallestofthreeno(self):
       a=self.getx()
       b=self.gety()
       c=self.getz()
       d=(a if a<c else c)if a<b else (b if b<c else c)
       return d
#main
a= Operatethreeno()
m=a.sumofthreeno()
print(' sum of three no:',m)
n=a.Productofthreeno()
print(' Product of three  no:',n)
o=a.Biggestofthreeno()
print('Biggest of  three no:',o)
p=a.Smallestofthreeno()
print('Smallest  of three no:',p)
a.setxyz(1000,1500,500)
x=a.sumofthreeno()
print(' sum of three no:',x)
y=a.Productofthreeno()
print(' Product of three  no:',y)
z=a.Biggestofthreeno()
print('Biggest of  three no:',z)
l=a.Smallestofthreeno()
print('Smallest  of three no:',l)