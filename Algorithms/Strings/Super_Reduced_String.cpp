#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    string s;
    cin>>s;
    int len;
    while(1==1)
    {len=s.size();
     string temp;
     int cnt=0;
    for(int i=0;i<len-1;i++)
        {
        if(s[i]==s[i+1])
        { s[i]=s[i+1]=45;cnt=1;}
    }
    for(int i=0;i<len;i++)
        {
        if(s[i]>=97 && s[i]<123)
            temp.push_back(s[i]);
    }
    s=temp;
     if(s.empty())
     {cout<<"Empty String";break;}
     if(cnt==0)
     {cout<<s;break;}
    }
    return 0;
}
