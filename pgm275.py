# Accessing two numbers using OOPs Inheritance
from pgm272 import Atwono
class Athreeno(Atwono):
    __z=None
    def __init__(self,a=100,b=200,c=300):
        self.__z=c
        Atwono.__init__(self,a,b)
    def setz(self,c=67):
        self.__z=c
    def setxyz(self,a=10,b=20,c=67):
        self.__z=c
        Atwono.setxy(self,a,b)
        
    def reset(self,c=0):
        Atwono.resetxy(self)
        self.__z=c
    def getz(self):
        return(self.__z)
    def getxyz(self):
        m=Atwono.getxy(self)
        return(m,self.__z)
    def printxyz(self):
        print(Atwono.printf(self),self.__z)
        
a=Athreeno()
a.printxyz()
a.setz(400)
a.printxyz()
a.reset()
a.setxyz(100,500,700)
a.printxyz()
a.setx(10)
a.sety(20)
a.setz(30)
n=a.getxyz()
print('value of x,y,z',n)
a.setxyz(4000,5000,9000)
q=a.getxyz()
print('value of x,y,z',q)
