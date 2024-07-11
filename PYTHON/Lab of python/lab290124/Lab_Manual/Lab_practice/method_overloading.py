class Calculator:
    def add(self, a,b=0,c=0):
        return a+b+c
    # def add(self,a,b):
    #     return a+b
    # def add(self,a,b,c):
    #     return a+b+c

# Usage
calc = Calculator()
print(calc.add(1))         # Output: 1
print(calc.add(1.5, 2))      # Output: 3
print(calc.add(1, 2, 3))   # Output: 6
