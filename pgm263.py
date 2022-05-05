# sum of two integer numbers in OOPs
class S2nos():
    __x=None
    __y=None
    __s=None
    def set(self,x=10,y=20):
       self.__x=x
       self.__y=y
    def find(self):
        self.__s=self.__x+self.__y
    def print(self):
         print('sum f two integer numbers',self.__s)
#main
a=S2nos()
a=S2nos(20)
a.set()
a.find()
a.print()
    