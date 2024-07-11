#include<bits/stdc++.h>
using namespace std;
//& this is reference this can be changed but if you just copy then it is not change the value

int main()
{
    pair<int,string> p;
    p=make_pair(1,"anchal"); //or p={2,"anchal"}
    cout<<p.first<<" "<<p.second<<endl;


pair<int,string> p1=p;//copy value  change actual value also
p1.first=6;
cout<<p1.first<<" "<<p1.second<<endl;
pair<int,string> &p2=p; //value change because of reference not actual value
p2.first=8;
cout<<p2.first<<" "<<p2.second<<endl;
cout<<p1.first<<" "<<p1.second<<endl;
vector<pair<int,int>> vec;
for(int i=0;i<4;i++)
{
    int x,y;
    cout<<"insert : ";
    cin>>x>>y;
    vec.push_back(make_pair(x,y));//{x,y}
}
cout<<"values : "<<endl;
for(int i=0;i<4;i++)
{
    cout<<vec[i].first<<" "<<vec[i].second<<endl;
}


}