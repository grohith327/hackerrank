#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int n;
    cin >> n;
    string B;
    cin >> B;
    int count=0;
    for(int i=0;i<n;i++)
        {
        int temp=i;
        if(B[temp]-'0'==0)
            {
            temp++;
            if(B[temp]-'0'==1)
                {
               temp++;
                if(B[temp]-'0'==0)
                    {
                    //cout<<i<<endl;
                    i=temp;
                    count++;
                }
            }
        }
    }
    cout<<count;
    return 0;
}
