#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    string s;
getline(cin,s);
int len=s.size();
int ar[26];
    for(int i=0;i<25;i++)
        ar[i]=0;
    for(int i=0;i<len;i++)
        {
        for(int j=65;j<91;j++)
            {
            if(s[i]==j)
                {
                ar[j-65]++;
            }
        }
        for(int j=97;j<123;j++)
            {
            if(s[i]==j)
                {
                ar[j-97]++;
            }
        }
    }
    int count=0;
    for(int i=0;i<26;i++)
        {
        if(ar[i]==0)
            {
            cout<<"not pangram";
            count=1;
            break;
        }
    }
    if(count==0)
        {
        cout<<"pangram";
    }
    return 0;
}
