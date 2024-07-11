#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"Enter size of an array : ";
    cin>>n;
    int arr[n];
    int sum=0;
    int total=0;
    for(int i=0;i<n-1;i++)
    {
        cin>>arr[i];
        sum=sum+arr[i];
    }
    total=(n*(n+1))/2;
   // cout<<"total  : "<<total<<" sum : "<<sum<<endl;
   cout<<"missing number : " <<total-sum;
    return 0;
}