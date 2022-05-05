# sum of 2-integer no's using OOPs
class S2nos():
    __x=None
    __y=None
    __s=None
    def __init__(self,x=10,y=20):
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
n=S2nos(40)
n.find()
n.printf()
q=S2nos(40,50)
q.find()
q.printf()
            
