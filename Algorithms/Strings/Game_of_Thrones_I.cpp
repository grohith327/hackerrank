#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
   
    string s;
    cin>>s;
     
    int flag = 0;
    // Assign Flag a value of 0 or 1 depending on whether or not you find what you are looking for, in the given string 
    int len=s.size();
    int count[26]={0};
    for(int i=0;i<len;i++)
        {
        count[s[i]-97]++;
    }
    if(len%2==0)
        {
        int cnt=0;
        for(int i=0;i<26;i++)
            {
           if(count[i]>0 && count[i]%2!=0)
               {
               cnt=1;
               break;
           }
        }
        if(cnt==0)
            flag=1;
    }
    else
        {
        int cnt=0;
        for(int i=0;i<26;i++)
            {
            if(count[i]>0 && count[i]%2!=0)
                {
                count[i]--;
                
                break;
            }
            
        }
        for(int i=0;i<26;i++)
            {
            if(count[i]>0 && count[i]%2!=0)
                {
                cnt=1;
                break;
            }
        }
        if(cnt==0)
            flag=1;
    }
    if(flag==0)
        cout<<"NO";
    else
        cout<<"YES";
    return 0;
}
