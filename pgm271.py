 # Sum of 2-integer no's using OOPs

class S2nos():
    __x=None
    __y=None
    __s=None
    def __init__(self,x=0,y=0):
       self.__x=x
       self.__y=y
    def setx(self,x=10):
       self.__x=x 
    def getx(self):
        return (self.__x)
    def printx(self):
        print(self.__x)
    def sety(self,y=20):
       self.__y=y
    def gety(self):
        return (self.__y)
    def printy(self):
        print(self.__y)
    def setxy(self,x=10,y=20):
       self.__x=x
       self.__y=y
    def getxy(self):
        return (self.__x,self.__y)
    def printxy(self):
       print(self.__x)
       print(self.__y)
    def reset(self,x=0,y=0):
        self.__x=x
        self.__y=y
    def find(self):
        self.__s=self.__x+self.__y
    def printf(self):
        print(self.__s)
#main
m=S2nos()
m.find()
m.printf()
m.setx(10)
m.sety(20)
m.find()
m.printf()
m.setxy(20,40)
m.find()
m.printf()