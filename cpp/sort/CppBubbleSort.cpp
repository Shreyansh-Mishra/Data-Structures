#include<bits/stdc++.h>
using namespace std;
int main()
{
int a[]={21,6,13,7,9};
int i,j,temp;
for(i=5;i>0;i--)
{
    for(j=0;j<i;j++)
    {
        if(a[j]>a[j+1])
        {
            temp=a[j];
            a[j]=a[j+1];
            a[j+1]=temp;
        }
    }
}
for(i=0;i<5;i++)
{
    cout<<a[i]<<" ";
}
return 0;
}