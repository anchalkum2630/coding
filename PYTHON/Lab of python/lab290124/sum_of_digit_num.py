n=1
while(n!=0):
    a=input("Enter a number to get sum : ")
    if(a.isdigit()):
        sum=0
        while(int(a)>0):
            nm=int(a)%10
            sum=sum+nm
            a=int(a)//10
            n=0
print(sum)