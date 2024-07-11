'''class teacher:
    def __init__(self):
        self.name="dheeraj"
        self.age="32"
        print(id(self))
    def display(self):
        print(self.name)
        print(self.age)
t1=teacher()
t1.display()
print(id(t1))
t2=teacher()
teacher("sujoy sir",55)'''


# class teacher:
#     institute="MANIT"                  
#     '''static variable'''
#     def __init__(self,Name,Age):
#         self.name=Name
#         self.age=Age
#         print(id(self))
#         '''instance method'''
#     def display(self):    
#         print(self.name)
#         print(self.age)
#     def fun(cls):
#         print(id(cls))
# '''t1=teacher("dheeraj sir",32)
# t1.display()
# print(teacher.institute)'''
# print(id(teacher))
# print(teacher.fun)

# def fun(a,b,c):
#     return a*b*c

# print(fun(100,32,44))




#user defined data types

# class complex:
#     def __init__(self,reala,imga):
#         self.real=reala
#         self.img=imga

#     def fun():
#         c1=pow(-1,1/2)
#         x=reala+c1*imga

# class demo:
#     def __init__(self):
#         self.x=12
#         self.y=100
#     def fun(self):
#         self.z=200

# d1=demo()
# d2=demo()
# print(d1.__dict__)
# d1.fun()
# print(d1.__dict__)
# print(d2.__dict__)
class complex:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    # def add(self):
       
    # int.__add__(self,x,y)
    # str.__add__(self,x,y)
    def __add__(a,b):
        real=c1.x+c2.x
        img=c1.y+c2.y
        return("{}+{}i".format(real,img))
c1=complex(6,8)
c2=complex(3,4)
print(c1+c2)





