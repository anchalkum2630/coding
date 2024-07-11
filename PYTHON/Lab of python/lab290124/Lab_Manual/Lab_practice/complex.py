class complex:
    def __init__ (self,reala,imga):
         self.real=reala
         self.img=imga
    def fun(self):
         c1=pow(-1,1/2)
         x=self.real+c1*self.img
    def display(self):
         print(f"{self.real} + {self.img}i")
c1=complex(5,6)
c1.display()
