#include<bits/stdc++.h>
using namespace std;
int main()
{
    int arr[4]={-1,-2,40,-5};
    priority_queue<int> pq(arr,arr+4);
    pq.push(6);
    pq.push(5);
    pq.push(3);
    pq.push(1);
    pq.push(9);
    while(!pq.empty())
    {
        cout<<pq.top()<<" ";
        pq.pop();
    }
    //pq.clear(); no function to clear
    cout<<"size : "<<pq.size();
}