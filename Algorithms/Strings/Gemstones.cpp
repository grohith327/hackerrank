#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin>>n;
    string s[n];
    for(int i=0;i<n;i++)
        cin>>s[i];
    int count[n][26]={{0}};
    for(int i=0;i<n;i++)
        {
        int len=s[i].size();
        for(int j=0;j<len;j++)
            {
            for(int k=97;k<123;k++)
                {
                if(s[i][j]==k)
                    {
                    count[i][k-97]++;
                }
            }
        }
    }
   /* for(int i=0;i<n;i++)
        {
        for(int j=0;j<26;j++)
            {
            cout<<count[i][j]<<" ";
        }
        cout<<endl;
    }*/
    
        int ans=0,cnt=0;
        for(int j=0;j<26;j++)
            {
            cnt=0;
            for(int i=0;i<n;i++)
                {
                if(count[i][j]>0)
                    {
                   cnt++; 
                }
                else
                    cnt=0;
            }
            if(cnt==n)
                ans++;
        }
    cout<<ans;
    
    return 0;
}
