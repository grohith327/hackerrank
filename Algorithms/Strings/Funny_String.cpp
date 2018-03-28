#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int q;
    cin>>q;
    for(int i=0;i<q;i++)
        {
        string s;
        cin>>s;
        string revs;
        revs=s;
        reverse(revs.begin(),revs.end());
        int cnt=0;
        int n=s.size();
        for(int i=1;i<n;i++)
            {
            if(abs(s[i]-s[i-1])!=abs(revs[i]-revs[i-1]))
                {
                cnt=1;
                break;
            }
        }
        if(cnt==0)
            cout<<"Funny\n";
        else
            cout<<"Not Funny\n";
            
    }

    return 0;
}

