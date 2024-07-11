#include<iostream>
using namespace std;
//time complexity=O(n^2)
void selection_sort(int a[],int size)
{
    int min;
    for(int i=0;i<size-1;i++)
    {
        //cout<<"Loop 1 : "<<endl;
        min=i;
        for(int j=i+1;j<size;j++)
        {
            if(a[min]>=a[j])
            {
                min=j;
            }
        }
        //cout<<"before : "<<a[i]<<" "<<a[min]<<endl;
                int temp=0;
                temp=a[i];
                a[i]=a[min];
                a[min]=temp;
                //cout<<"after : "<<a[i]<<" "<<a[min]<<endl;
        //cout<<endl<<" Array"<<i<<" : ";
        //for(int k=0;k<size;k++)
    //{
    //    cout<<a[k]<<" ";
    //}
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
    selection_sort(arr,n);
    cout<<"Sorted Array : ";
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}