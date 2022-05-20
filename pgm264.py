# area of circle using OOPs
class Aofcircle():
    __r=None
    __a=None
    def set(self):
       self.__r=7
    def find(self):
        self.__a=22/7*self.__r**2
    def printf(self):
         print("area of ciecle:",self.__a)
#main
m=Aofcircle()
m.set()
m.find()
m.printf()