#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<math.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int q;
    cin>>q;
    for(int i=0;i<q;i++)
        {
       string s;
        cin>>s;
        int len=s.size();
        string l,r;
        for(int j=0;j<len/2;j++)
            {
            l.push_back(s[j]);
        }
        for(int j=len/2;j<len;j++)
            {
            r.push_back(s[j]);
        }
        int count1[26]={0};
        int count2[26]={0};
        int len1=l.size();
        int len2=r.size();
        if(len1!=len2)
            {
            cout<<"-1\n";
            continue;
        }
        for(int j=0;j<len1;j++)
            {
            count1[l[j]-97]++;
        }
        for(int j=0;j<len2;j++)
            {
            count2[r[j]-97]++;
        }
        int num=0;
        for(int j=0;j<26;j++)
            {
            num+=abs(count1[j]-count2[j]);
        }
        cout<<num/2<<endl;
       // cout<<l<<" "<<r;
        //cout<<endl;
    }
    return 0;
}
