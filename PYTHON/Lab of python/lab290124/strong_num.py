total=0
n=1
while(n!=0):
    b=input("Enter a number to check it is strong number : ")
    if(b.isdigit()):
        a=int(b)
        while(a>0):
            nm=a%10
            'print(nm)'
            fact=1
            i=1
            for i in range(1,nm+1):
                fact=i*fact
            'print(fact)'
            'print(a)'
            total=total+fact
            a=a//10
            n=0
        if(total==int(b)):
            print(total)
            print("it is strong number")
        else:
            print("It is not a strong number")