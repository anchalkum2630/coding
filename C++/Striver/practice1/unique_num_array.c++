#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cout<<"Enter size of an array : ";
    cin>>n;
    cout<<"Enter zero and one in array : ";
    int arr[n];
    int sum=0;
    int total=0;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
       // sum=sum+arr[i];
    }
    int xorr=0;
    for(int i=0;i<n;i++)
    {
        xorr=xorr^arr[i];
    }
    cout<<"unique number : "<<xorr;
}