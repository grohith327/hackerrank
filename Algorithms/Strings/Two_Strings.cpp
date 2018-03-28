#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
        {
        string s1,s2;
        cin>>s1>>s2;
        int count1[26]={0};
        int count2[26]={0};
        int len1,len2;
        len1=s1.size();
        len2=s2.size();
        for(int j=0;j<len1;j++)
            {
            for(int k=97;k<123;k++)
                {
                if(s1[j]==k)
                    {
                    count1[k-97]++;
                    break;
                }
            }
        }
        for(int j=0;j<len2;j++)
            {
            for(int k=97;k<123;k++)
                {
                if(s2[j]==k)
                    {
                    count2[k-97]++;
                    break;
                }
            }
        }
        int cnt=0;
        for(int j=0;j<26;j++)
            {
            if(count1[j]>0 && count2[j]>0)
                {
                cnt=1;
                cout<<"YES\n";
                break;
            }
        }
        if(cnt==0)
            {
            cout<<"NO\n";
        }
    }
    return 0;
}
