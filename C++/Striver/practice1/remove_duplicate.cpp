#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cout<<"Enter size of an array : ";
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        int num;
        cin>>num;
        arr[i]=num;
    }
    map<int,int> mp;
    for(int i=0;i<n;i++)
    {
        if(mp[arr[i]])
        {
            continue;
        }
        mp[arr[i]]++;
    }
    for(auto it:mp)
    {
        cout<<it.first<<" ";
    }
}