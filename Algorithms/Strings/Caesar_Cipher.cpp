#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;
    string s;
    cin >> s;
    int k;
    cin >> k;
    int num;
    for(int i=0;i<n;i++)
        {
        num=s[i];
        if(num>=65 && num<91)
            {
            num=num+k;
            while(num>=91)
                {
                num=num-26;
            }
        }
        if(num>=97 && num<123)
            {
            num=num+k;
            while(num>=123)
                {
                num=num-26;
            }
               
        }
        s[i]=num;
    }
    cout<<s;
    return 0;
}
