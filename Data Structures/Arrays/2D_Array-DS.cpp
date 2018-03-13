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
  int ar[6][6];
    for(int i=0;i<6;i++)
        {
        for(int j=0;j<6;j++)
            {
            cin>>ar[i][j];
        }
    }
    
   vector<int> pos;
    for(int i=0;i<4;i++)
        {
        int sum=0;
        for(int j=0;j<4;j++)
            {
            sum=0;
            sum+=ar[i][j]+ar[i][j+1]+ar[i][j+2]+ar[i+1][j+1]+ar[i+2][j]+ar[i+2][j+1]+ar[i+2][j+2];
            pos.push_back(sum);
        }
        
        //cout<<sum<<endl;
    }
    sort(pos.begin(),pos.end());
    reverse(pos.begin(),pos.end());
    cout<<pos[0];
    return 0;
}
