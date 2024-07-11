#include<bits/stdc++.h>
using namespace std;
int main()
{
    queue<int> q;
    q.push(6);
    q.push(5);
    q.push(3);
    q.push(1);
    cout<<"front : "<<q.front()<<" back : "<<q.back()<<endl;
    cout<<"size : "<<q.size();
    q.pop();
    cout<<"front : "<<q.front();
}