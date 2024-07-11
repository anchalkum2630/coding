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
    int count=0,max=0;
    for(int i=0;i<n;i++)
    {
        //cout<<"i running : "<<i<<endl;
       // cout<<" array number : "<<arr[i]<<endl;
        if(arr[i]==1)
        {
            count++;
            //cout<<"array enter : "<<i<<"count : "<<count<<endl;;
            
            if(max<count)
            {
                max=count;
            }
        }
        else{
            count=0;
        }
    }
    cout<<"maximum frequency of one : "<<max;
}