#include<iostream>
#include<vector>
using namespace std;
//v.push_back
//v.at(i)
//v.size()
//v.container()
//v.resize(give the size you want to make last element removed)
//v.shrink_to_fit(it also reduces memory)
//v.empty()
//v.swap()
//v.assign(k,i)->k=no.of times repeat i=value
//v.insert(a,b)->a=index and b=value
//v.rbegin()->return a reverse iterater we can print reverse no
//v.rend()->it is just as begin
//reverse(v,begin(),v.end())
//v.data()->return iterator of the first element in vector
//v1.clear()
//v1.erase()
//sort(start,end)


int main()
{
    vector<int> v;
    for(int i=0;i<17;i++)  //int one container =4 8 16 this increases
    {
        v.push_back(i*100);
    }
    //print the numbers
    for(int i=0;i<v.size();i++)
    {
        cout<<v.at(i)<<endl;
    }
    //to check vector is empty
    if(v.empty()==true)
    {
        cout<<"Vector is empty"<<endl;
    }
    else{
        cout<<"Vector is not empty"<<endl;
    }
    cout<<v.size();
    cout<<endl<<v.capacity()<<endl;


    //iterator v.begin()->return address of the first element in vector
    //iterator v.end()->return address of the last element in vector
    vector<int>::iterator x;
    for(x=v.begin();x!=v.end();x++)
    {
        cout<<*x<<" ";
    }


//to initialize a same valur multiple times
vector <int> v1;
v1.assign(5,10);    // assign 10   5 times
v1.insert(v1.begin(),20);
//v1.clear();
for(int i=0;i<v1.size();i++)
{
    cout<<endl<<v1[i];
}
cout<<endl<<v1.data();


}
