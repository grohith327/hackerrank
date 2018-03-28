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
    string a;
    cin >> a;
    string b;
    cin >> b;
    int count1[26]={0};
    int count2[26]={0};
    for(int i=0;i<a.size();i++)
        count1[a[i]-97]++;
    for(int j=0;j<b.size();j++)
        count2[b[j]-97]++;
    int nod=0;
    for(int i=0;i<26;i++)
        {
        if(count1[i]!=count2[i])
            {
            nod+=abs(count1[i]-count2[i]);
        }
    }
    cout<<nod;
    return 0;
}
