#include<bits/stdc++.h>
using namespace std;
int main()
{
    deque<int> q;
    q.push_back(6);
    q.push_front(5);
    q.push_front(3);
    q.push_back(1);
    cout<<"front : "<<q.front()<<" back : "<<q.back()<<endl;
    q.push_back(5);
    cout<<"size : "<<q.size();
    cout<<endl;
    while(!q.empty())
    {
        cout<<q.front();
        q.pop_front();
    }
    /*cout<<endl;
    q.pop_back();
    cout<<"back : "<<q.back();
    cout<<endl;
    while(!q.empty())
    {
        cout<<q.front();
        q.pop_front();
    }*/
}