'''class parent:
    def __init__ (self,x,y):
        self.__x=x  #double _ is used in private self.__x=x
        self.__y=y
    def print(self):
        print("x = ",self.__x)
        print("y = ",self.__y)
class child(parent):
    def __init__ (self,x,y,a,b):
      super().__init__(x,y)
      self.a=a
      self.b=b
    def print(self):
        #print("x = ",self.x)
        #print("y = ",self.y)
        super().print()
        print("a = ",self.a)
        print("b = ",self.b)
mca=child(10,20,30,40)
mca.print()'''



class parent:
    def __init__(self, x, y):
        self.__x=x
        self.y=y
    # def print(self):
    #     print("x==",self.__x)
    #     print("y==",self.y)
       
class child(parent):
    def __init__(self,x,y,a,b):
        super().__init__(x, y)
        self.a=a
        self.b=b
    # def print(self):  // when function is not available in child then it check in parent class this is called method overriding
    #     #print("x==",self.x)
    #     #print("y==",self.y)
    #     self.print()
    #     print("a==",self.a)
    #     print("b==",self.b)

mca=child(10,20,30,40)
mca.print()
