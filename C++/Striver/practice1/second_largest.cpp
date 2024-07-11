#include<bits/stdc++.h>
using namespace std;
int main()
{
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
    /*tc->O(n*log^n),sc->O(1)
    sort(arr,arr+n);
    cout<<"second largest :"<<arr[n-2];*/

    
    //second approach tc->O(n),sc->O(1)
    int largest=arr[0];
    int secondlargest=-1;
    for (int i=0;i<n;i++)
    {
        if(arr[i]>largest)
        {
            secondlargest=largest;
            largest=arr[i];
        }
        if(arr[i]<largest&&arr[i]>secondlargest)
        {
            secondlargest=arr[i];
        }
    }
    cout<<"second largest :"<<secondlargest;
}