#include<iostream>
using namespace std;
void f(int num){
    if (num==0){
        return;
    }
    cout<<num<<" ";
    f(num-1);
    cout<<num<<" ";
}
// void f1(){
//     cout<<"happy ";
//     f1();
// }
int sum(int num,int &res){
    if(num==0){
        return 0;
    }
    res=num+sum(num-1,res);
    return res;
}
int sum1(int num){
    if(num==0){
        return 0;
    }
    return num+sum1(num-1);
}
int fib(int n)
{
    if (n <= 1)
        return n;
    return fib(n - 1) + fib(n - 2);
}
int main(){
    f(5);
    // f1();
    int res=0;
    sum(100,res);
    cout<<endl<<"sum : "<<res;
    cout<<endl<<"sum : "<<sum1(5);
    cout <<endl<<"the Fibonacci Number: " << fib(9);
    return 0;
}