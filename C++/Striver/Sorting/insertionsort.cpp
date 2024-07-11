#include<iostream>
using namespace std;
//time complexity->O(n^2)//best case->O(n)
void insertion_sort(int a[],int size)
{
    for(int i=0;i<size;i++)
    {
        int j=i;
        while(j>0&&a[j-1]>a[j])
        {
           // cout<<endl<<"i : "<<i<<" j : "<<j<<endl;
            if(a[j]<a[j-1])
            {
                swap(a[j],a[j-1]);
            }
            j--;
        }
       /* cout<<endl<<"Sorted"<<i<<" : ";
        for(int k=0;k<size;k++)
        {
            cout<<a[k];
        }*/
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
    insertion_sort(arr,n);
    cout<<"Sorted Array : ";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}