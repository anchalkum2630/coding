//how many times a number appers in an array
#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter size of an array : ";
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cout<<"Enter number : ";
        cin>>arr[i];
    }

    //precompute
    int hash[13]={0};
    for(int i=0;i<n;i++)
    {
        if(arr[i] >= 0 && arr[i] < 13) {
            hash[arr[i]]++;}
    }

    //Enter the number you want to find
    int start=0;
    int find;
    while(start!=1)
    {
        cout<<"Enter number you want to find how many times it repeat in an array : ";
        cin>>find;
        cout<<"Number of times "<<find<<" repeat : "<<hash[find];
        cout<<endl<<"press 0 to continue and press 1 to terminate : ";
        cin>>start;
    }
    return 0;
}