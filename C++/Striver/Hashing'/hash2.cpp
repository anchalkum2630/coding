#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cout<<"Enter string : ";
    cin>>s;
   /* int hash[256]={0};
    for(int i=0;i<s.size();i++)
    {
        hash[s[i]]++;
    }
    int start=0;
    char find;
    while(start!=1)
    {
        cout<<"Enter character you want to find how many times it repeat in an array : ";
        cin>>find;
        cout<<"Number of times "<<find<<" repeat : "<<hash[find];
        cout<<endl<<"press 0 to continue and press 1 to terminate : ";
        cin>>start;
    }*/

    //another way to do this question

    map<char,int> ans;
    for(int i=0;i<s.size();i++)
    {
          ans[s[i]]++;
    }
    for(auto it:ans)
    {
        cout<<it.first<<" "<<it.second<<endl;
    }
    int start=0;
    char find;
    while(start!=1)
    {
        cout<<"Enter character you want to find how many times it repeat in an array : ";
        cin>>find;
        cout<<"Number of times "<<find<<" repeat : "<<ans[find];
        cout<<endl<<"press 0 to continue and press 1 to terminate : ";
        cin>>start;
    }
    return 0;
}