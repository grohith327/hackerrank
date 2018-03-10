#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
   int ar[1000011];
    int n,m;
    cin>>n;
    int num;
    for(int i=0;i<1000011;i++)
        {
        ar[i]=0;
    }
    for(int i=0;i<n;i++)
        {
        cin>>num;
        ar[num]++;
    }
    cin>>m;
    for(int i=0;i<m;i++)
        {
        cin>>num;
        ar[num]--;
    }
    for(int i=0;i<1000011;i++)
        {
        if(ar[i]!=0)
            cout<<i<<" ";
    }
    return 0;
}

