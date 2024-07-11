n=1
while(n!=0):
    a=input("Enter number to find a^b , a : ")
    if(a.isdigit()):
        b=input("b : ")
        if(b.isdigit()):
            power=int(a)**int(b)
            n=0
print(power)
