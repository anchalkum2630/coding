#include<iostream>
using namespace std;
template<class T1=int,class T2=int,class T3=int>
class Multi
{
    public:
    T1 x;
    T2 y;

    T3 multiple()
    {
        return x*y;
    }
};
int main()
{
    Multi<int,int,int> m1;
    m1.x=5;
    m1.y=8;
    cout<<"Result = "<<m1.multiple();
    return 0;
}