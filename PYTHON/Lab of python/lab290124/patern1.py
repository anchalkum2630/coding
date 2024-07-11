n=1
while(n!=0):     
    a=input("Enter a number to make triangle : ")
    if(a.isdigit()):
        n=0
        i=1
        for i in range(int(a)+1):
            for j in range(i):
                print("* ",end=" ")
            print() 