#Area of circle using  OOOPs
class Aofcircle():
    __r=None
    __a=None
    def __init__(self,r):
        self.__r=r
    def find(self):
        self.__a=22/7*self.__r**2
    def print(self):
        print(self.__a)
#main
m=Aofcircle(7)
m.find()
m.print()