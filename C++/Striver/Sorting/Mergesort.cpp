#include<bits/stdc++.h>
using namespace std;
//time complexity->O(n*logn)//worst->O(n)//space complexity->O(n)
void Merge(vector<int> &arr,int low,int mid,int high)
{
    vector<int> temp;
     int left=low;
     int right=mid+1;
     while(left<=mid&&right<=high)
     {
         if(arr[left]<arr[right])
         {
             temp.push_back(arr[left]);
             left++;
         }
         else{
             temp.push_back(arr[right]);
             right++;
         }
     }
     while(left<=mid)
     {
         temp.push_back(arr[left]);
         left++;
     }
     while(right<=high)
     {
         temp.push_back(arr[right]);
         right++;
     }
     for(int i=low;i<=high;i++)
     {
         arr[i]=temp[i-low];
     }
     
}
void Merge_sort (vector<int> &a,int low,int high)
{
    //cout<<" call "<<low<<" "<<high;
      if(low>=high)
      return;
      int mid=(low+high)/2;
      Merge_sort(a,low,mid);
      Merge_sort(a,mid+1,high);
      Merge(a,low,mid,high);
}
int main()
{
    int n;
    cout<<"Enter the size of the array : ";
    cin>>n;
    vector<int> vec;
    for(int i=0;i<n;i++)
    {
        int num;
        cin>>num;
        vec.push_back(num);
    }
    Merge_sort(vec,0,n-1);
    cout<<"Sorted Array : ";
    for(int i=0;i<n;i++)
    {
        cout<<vec[i]<<" ";
    }
    return 0;
}