#include<bits/stdc++.h>
using namespace std;
int main()
{
    set<int> s;
    s.insert(3);
    s.insert(4);
    s.insert(3);
    s.insert(6);
    s.insert(2);
    if(s.count(6)){
        cout<<"prsent";
    }
    else{
        cout<<"not present";
    }
    s.erase(3);
    for(auto x:s)//asending order
    {
        cout<<x<<" ";
    }
}