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
        cin>>arr[i];
    }
    int max=arr[0];
    int count=0;
    for(int i=1;i<n;i++)
    {
        if(arr[i]<max)
        {
            count++;
            //max=arr[i];
        }
        if(count>=1)
        {
            cout<<"not in sorted way ";
            return 0;
        }
        else
        {
            cout<<"in sorted way";
            return 0;
        }
    }
}