# Biggest of three numbers using OOPs

class Bofthree():
    __x=None
    __y=None
    __z=None
    __b=None
    def __init__(self,x=5,y=6,z=7):
       self.__x=x
       self.__y=y
       self.__z=z
    def find(self):
        self.__b=(self.__x if self.__x>self.__z else self.__z)if self.__x>self.__y else(self.__y if self.__y>self.__z else self.__z)
    def printf(self):
         print(self.__b)
#main
m=Bofthree()
m.find()
m.printf()
n=Bofthree(15)
n.find()
n.printf()
q=Bofthree(6,3,13)
q.find()
q.printf()