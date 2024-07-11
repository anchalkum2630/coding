#include<bits/stdc++.h>
using namespace std;
int main()
{
    stack<int> s;
    s.push(1);
    s.push(6);
    s.push(5);
    s.push(3);
    cout<<"top= "<<s.top()<<endl;
    s.pop();
    cout<<"top= "<<s.top()<<endl<<"size : "<<s.size()<<endl;
    if(s.empty())
    {
        cout<<"empty"<<endl;
    }
    else
    {
        cout<<"not empty"<<endl;
    }
    while(!s.empty())
    {
        int val=s.top();
        cout<<val<<" ";
        s.pop();
    }

}