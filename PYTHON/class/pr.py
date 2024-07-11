# import keyword
# print(keyword.kwlist)
# i=0
# sum=0
# l=eval(input("enter a number: "))
# for i in l:
#     sum=sum+i
# print(sum)


#Destructor -> way to write __del__(self)
# class student:
#     def __init__(self,a,b):
#         self.x=a
#         self.y=b
#         print("object created")
#     def __del__(self):
#         print("Object delete")
# ob1=student(10,20)
# ob2=ob1 #it makes
# del ob1

# class Employee:
  
#     # Initializing
#     def __init__(self):
#         print('Employee created')
  
#     # Calling destructor
#     def __del__(self):
#         print("Destructor called")
  
# def Create_obj():
#     print('Making Object...')
#     obj = Employee()
#     print('function end...')
#     return obj
  
# print('Calling Create_obj() function...')
# obj = Create_obj()
# print('Program End...')


#file handling ,error,exception

#a=b  //b is not defined

# try and catch method
try:
    a=int(input())
    b=int(input())
    print(a/b)
except ValueError:
    print("wrong..value must be in number")
except ZeroDivisionError:
    print("wrong..denominator should not be zero")