#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    string s;
    cin>>s;
    int ar[26]={0};
    int len=s.size();
    for(int i=0;i<len;i++)
        {
        for(int j=0;j<26;j++)
            {
            if(s[i]==97+j)
                {
                ar[j]++;
            }
        }
    }
  /*  for(int i=0;i<26;i++)
        {
        cout<<ar[i]<<endl;
    }*/
    int num,count=0,pos=0;
    for(int i=0;i<26;i++)
        {
        if(ar[i]==0)
            continue;
        
        count=0;
        for(int j=i+1;j<26;j++)
            {
            if(ar[i]==ar[j])
                count++;
        }
        if(num<count)
        { num=count;pos=i;}
        
    }
    count=0;
    for(int i=0;i<26;i++)
        {
        if(ar[i]>0 && ar[i]!=ar[pos])
            {
            count++;
        }
    }
    if(count<=1)
        cout<<"YES";
    else
        cout<<"NO";
    
    return 0;
}
