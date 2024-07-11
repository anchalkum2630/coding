#include<bits/stdc++.h>
using namespace std;
//time complexity O(n^2) //best case->O(n)
void bubble_sort(int a[],int size)
{
    for(int i=size-1;i>=0;i--)
    {
        int count=0;
        for(int j=0;j<=i;j++)
        {
            
            if(a[j]>a[j+1])
            {
                swap(a[j],a[j+1]);
                count++;
            }          
        }
        if(count==0)
            {
                break;
            } 
       /* cout<<endl<<"count : "<<count;
        cout<<endl<<"Sorted"<<i<<" : ";
        for(int j=0;j<size;j++)
        {
            cout<<a[j];
        }
*/
    }

}
int main()
{
    int n;
    cout<<"Enter the size of the array : ";
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    bubble_sort(arr,n);
    cout<<"Sorted Array : ";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;

}