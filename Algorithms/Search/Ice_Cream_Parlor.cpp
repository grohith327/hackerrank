#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


    


int main() {
    int t;
    cin>>t;
    int temp;
    for(int i=0;i<t;i++)
        {
        int n,m,a,b;
        cin>>m>>n;
        int ar[n];
        for(int j=0;j<n;j++)
            {
            cin>>ar[j];
        }
       
       
        for(int j=0;j<n;j++)
            {
            for(int k=j+1;k<n;k++)
               {
                if(ar[j]+ar[k]==m)
                    {
                    a=j;
                    b=k;
                    break;
                }
            }
        }
        if(a<b)
        cout<<a+1<<" "<<b+1<<endl;
        else
            cout<<b+1<<" "<<a+1<<endl;
    }
    
return 0;

}

