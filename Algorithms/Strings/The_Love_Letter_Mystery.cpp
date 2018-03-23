#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
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
        int nor=0,r=0;
        
           
            for(int j=0;j<len/2;j++)
                {
                if(s[j]<s[len-1-j])
                    {
                    r=s[len-1-j]-s[j];
                    s[len-1-j]=s[len-1-j]-r;
                    nor+=r;
                }
                else if(s[j]>s[len-1-j])
                    {
                    r=s[j]-s[len-1-j];
                    s[j]=s[j]-r;
                    nor+=r;
                }
                else
                    ;
                  
                
            }
        
        cout<<nor<<endl;
    }
    return 0;
}
