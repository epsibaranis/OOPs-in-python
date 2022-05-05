# Biggest of three numbers using OOPs

class Bofthree():
    __x=None
    __y=None
    __z=None
    __b=None
    def set(self):
       self.__x=5
       self.__y=6
       self.__z=7
    def find(self):
        self.__b=(self.__x if self.__x>self.__z else self.__z)if self.__x>self.__y else(self.__y if self.__y>self.__z else self.__z)
    def printf(self):
         print(self.__b)
#main
a= Bofthree()
a.set()
a.find()
a.printf()