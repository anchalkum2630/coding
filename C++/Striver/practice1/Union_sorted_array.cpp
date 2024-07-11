#include<bits/stdc++.h>
using namespace std;
//sorted array to give print common element
int main()
{
    int n1,n2;
    cout<<"first array size : ";
    cin>>n1;
    cout<<"second array size : ";
    cin>>n2;
    int arr1[n1];
    int arr2[n2];
    for(int i=0;i<n1;i++)
    {
        cin>>arr1[i];
    }
    for(int i=0;i<n2;i++)
    {
        cin>>arr2[i];
    }

    vector<int> ans;
            int i=0,j=0;
            while(i<n1&&j<n2)
            {
                int common=0;
                int minVal=min(arr1[i],arr2[j]);
                //cout<<"val1 : "<<minVal<<endl;
                if(arr1[i]==arr2[j])
                {
                    ans.push_back(arr1[i]);
                    //common=A[i];
                    i++;
                    j++;
                    cout<<"arr1 : "<<arr1[i]<<"val2 : "<<minVal<<endl;
                }
                    if(arr1[i]==minVal)i++;
                    if(arr2[j]==minVal)j++;
                   // if(C[k]==minVal)k++;
            }
            ans.erase(unique(ans.begin(), ans.end()), ans.end());
            for(int j=0;j<ans.size();j++)
            {
                cout<<ans[j]<<" ";
            }
    return 0;
}