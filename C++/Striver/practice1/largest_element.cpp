#include<bits/stdc++.h>
using namespace std;
int main()
{
    //time complexity->O(n),  space complexity->O(1)
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
    /*int max=arr[0];
    for(int i=0;i<n;i++)
    {
        if(max<arr[i])
        {
            max=arr[i];
        }
    }*/
    //second approach time complexity->O(n*logn),  space complexitity->1
    sort(arr,arr+n);
    int max=arr[n-1];
    cout<<"Largest element : "<<max;
}