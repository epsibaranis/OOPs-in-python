# Accessing two numbers using OOPs

class Atwono():
    __x=None
    __y=None
    def __init__(self,a=10,b=20):
       self.__x=a
       self.__y=b
    def setx(self,a=0):
       self.__x=a    
    def sety(self,b=0):
       self.__y=b
    def setxy(self,a=0,b=0):
       self.__x=a
       self.__y=b
    def resetxy(self,a=0,b=0):
       self.__x=a
       self.__y=b
    def getx(self):
        return (self.__x)
    def gety(self):
        return (self.__y)
    def getxy(self):
        return (self.__x,self.__y)
    def print(self):
        print(self.__x,self.__y)
