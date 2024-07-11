#include<iostream>
using namespace std;
template <class t>
t Max(t x,t y)
{
    return x>y?x:y;
}
int main()
{
    char Value1,Value2;
    cout<<"Enter two values to compare : ";
    cin>>Value1>>Value2;
    cout<<"Max Value : "<<Max<char>(Value1,Value2);

}