#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin>>n;
    int ar[n];
    for(int i=0;i<n;i++)
        {
        cin>>ar[i];
    }
    int count[n][2];
    int k=1;
    int cnt;
    count[0][0]=ar[0];
    for(int i=1;i<n;i++)
        {
        cnt=0;
        for(int j=0;j<k;j++)
            {
            if(count[j][0]==ar[i])
                {
                cnt=1;
                break;
            }
        }
        if(cnt==0)
            {
            count[k][0]=ar[i];
            k++;
        }
    }
    
    for(int i=0;i<k;i++)
        {
        cnt=0;
        for(int j=0;j<n;j++)
            {
            if(count[i][0]==ar[j])
                {
                cnt++;
            }
        }
        count[i][1]=cnt;
    }
    for(int i=0;i<k;i++)
        {
        if(count[i][1]!=2)
            {
            cout<<count[i][0];
            break;
        }
    }
    
    return 0;
}
