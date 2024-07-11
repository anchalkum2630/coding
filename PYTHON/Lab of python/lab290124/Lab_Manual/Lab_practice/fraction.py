class fraction:
    def __init__(self,a=0,b=1):
        self.first=a
        self.second=b
    def display(self):
        print(self.first,"/",self.second)
    def normalize(self):
        min=0
        i=1
        div=0
        if(self.first>self.second):
            min=self.second
        else:
            min=self.first
        for i in range(min,1,-1):
            if(self.first%i==0 and self.second%i==0 ):
                div=i
                break
        self.first=self.first//div
        self.second=self.second//div
s1=fraction(12,8)
s1.normalize()
s1.display()
# Demonstrating for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I love", fruit)
# Global variable
global_var = 10

def function():
    # Local variable
    local_var = 5
    print("Inside the function: global_var =", global_var)  # Accessing global variable
    print("Inside the function: local_var =", local_var)    # Accessing local variable

# Call the function
function()

print("Outside the function: global_var =", global_var)    # Accessing global variable outside the function
# Uncommenting the next line will result in an error since local_var is not accessible outside the function.
# print("Outside the function: local_var =", local_var)    # Accessing local variable outside the function
