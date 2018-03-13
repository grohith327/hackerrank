#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

int main(void) {

    int m;
    cin>>m;
    char grid[m][m];
    for(int i=0;i<m;i++)
        {
        for(int j=0;j<m;j++)
            cin>>grid[i][j];
    }
    int pi,pj,mi,mj;
    for(int i=0;i<m;i++)
        {
        for(int j=0;j<m;j++)
            {
            if(grid[i][j]=='p')
               {
                pi=i;
                pj=j;
               
            } 
            if(grid[i][j]=='m')
                {
                mi=i;
                mj=j;
            }
        }
    }
    int a,b;
    a=mi-pi;
    b=mj-pj;
    if(a<0)
        {
        for(int i=0;i<abs(a);i++)
            cout<<"DOWN\n";
        
    }
    if(a>0)
        {
        for(int i=0;i<a;i++)
            cout<<"UP\n";
    }
    if(b<0)
        {
        for(int i=0;i<abs(b);i++)
            cout<<"RIGHT\n";
    }
    if(b>0)
        {
        for(int i=0;i<b;i++)
            cout<<"LEFT\n";
    }

    return 0;
}
