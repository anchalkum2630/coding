#include<bits/stdc++.h>
using namespace std;
int main()
{
    list<int>l1;
    l1.push_back(7);
    l1.push_back(6);
    l1.push_back(3);
    l1.push_front(9);
    l1.push_back(0);
    l1.push_back(1);
    list<int> ::iterator it;
    for(it=l1.begin();it!=l1.end();it++)
    {
         cout<<*(it)<<" ";//*->value at;
    }
    cout<<endl<<l1.front()<<" "<<l1.back()<<endl;
    l1.reverse();
    for(it=l1.begin();it!=l1.end();it++)
    {
         cout<<*(it)<<" ";//*->value at;
    }
    cout<<endl;
    l1.sort();
    for(it=l1.begin();it!=l1.end();it++)
    {
         cout<<*(it)<<" ";//*->value at;
    }
}