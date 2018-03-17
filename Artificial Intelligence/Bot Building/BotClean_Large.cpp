#include<iostream>
#include<vector>
using namespace std;
int main(void) {
    int r,c,h,w;
    cin>>r>>c>>h>>w;
    char grid[h][w];
    for(int i=0;i<h;i++)
        {
        for(int j=0;j<w;j++)
            {
            cin>>grid[i][j];
        }
    }
        int pos[2];
        
        for(int i=0;i<h;i++)
            {
            for(int j=0;j<w;j++)
                {
                if(grid[i][j]=='d')
                    {
                    pos[0]=i;
                    pos[1]=j;
                    break;
                }
                //cout<<grid[i][j]<<" ";
            }
            //cout<<endl;
        }
 //   cout<<pos[0]<<" "<<pos[1];
        int a=r-pos[0];
        int b=c-pos[1];
        if(a<0)
        {
        
            cout<<"DOWN\n";
        
    }
    else if(a>0)
        {
      
            cout<<"UP\n";
    }
    else if(b<0)
        {
        
            cout<<"RIGHT\n";
    }
    else if(b>0)
        {
       
            cout<<"LEFT\n";
    }
        else
            ;
     if(a==0 && b==0)
         {
         cout<<"CLEAN";
     }

            
            
    
   
    
    return 0;
    }
