#include <iostream>
#include <vector>
using namespace std;

int main(void) {

    int n, r, c;
   cin>>n>>r>>c;
    char grid[n][n];
    for(int i=0;i<n;i++)
        {
        for(int j=0;j<n;j++)
            {
            cin>>grid[i][j];
        }
    }
    int pi,pj;
    for(int i=0;i<n;i++)
        {
        for(int j=0;j<n;j++)
            {
            if(grid[i][j]=='p')
                {
                pi=i;
                pj=j;
            }
        }
    }
    int a,b;
    a=r-pi;
    b=c-pj;
    if(a==0)
        {
        if(b>0)
            {
            cout<<"LEFT";
            
        }
        else
            cout<<"RIGHT";
    }
    else if(b==0)
        {
        if(a>0)
            {
            cout<<"UP";
            
        }
        else
            cout<<"DOWN";
    }
    else if(a>0)
        cout<<"UP";
    else if(a<0)
        cout<<"DOWN";
    else if(b>0)
        cout<<"LEFT";
    else if(b<0)
        cout<<"RIGHT";
    else
        ;
        
    return 0;
}
