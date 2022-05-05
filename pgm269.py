# sum of 2-integer no's using OOPs
class S2nos():
    __x=None
    __y=None
    __s=None
    def __init__(self,a=10,b=20):
        self.__a=10
        self.__b=20
    def find(self):
        self.__s=self.__a+self.__b
    def print(self):
        print(self.__s)
#main
a=S2nos()
a.find()
a.print()
b=S2nos(a)
b.find()
b.print()
c=S2nos(a,b)
c.find()
c.print()