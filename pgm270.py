# Biggest of three numbers using OOPs
class Bofthreeno():
    __x=None
    __y=None
    __z=None
    __b=None
    def __init__(self,x=10,y=20,z=30):
       self.__x=10
       self.__y=20
       self.__z=30
    def find(self):
        self.__b=(self.__x if self.__x>self.__z else self.__z)if self.__x>self.__y else(self.__y if self.__y>self.__z else self.__z)
    def print(self):
         print("Biggest of three numbers:",self.__b)
#main
a=Bofthreeno()
b=Bofthreeno(a)
c=Bofthreeno(b)
d=Bofthreeno(c)
a.find()
a.print()
b.find()
b.print()
c.find()
c.print()
d.find()
d.print()