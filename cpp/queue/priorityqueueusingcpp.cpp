/*priority queue stores element in either increasing or decreasing order*/

#include<bits/stdc++.h>
using namespace std;
int main(){
    priority_queue<int> q1;
    priority_queue<int,vector<int>,greater<int>> q2;  //to store in increasing order
    
    //decreasing order
    q1.push(23);
    q1.push(12);
    q1.push(1);
    q1.push(41);
    q1.push(29);
    q1.push(0);
    
    //increasing order
    q2.push(23);
    q2.push(12);
    q2.push(1);
    q2.push(41);
    q2.push(29);
    q2.push(0);
while(!q1.empty()){
    cout<<q1.top()<<" ";
    q1.pop();
}
cout<<endl;
while(!q2.empty()){
    cout<<q2.top()<<" ";
    q2.pop();
}
}