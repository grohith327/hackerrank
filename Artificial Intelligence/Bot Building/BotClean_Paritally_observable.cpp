#include<iostream>
#include<vector>
using namespace std;

int main(void) {
    int r,c;
    char grid[5][5];
    cin>>r>>c;
    int count=0;
    for(int i=0;i<5;i++)
        {
        for(int j=0;j<5;j++)
            {
            cin>>grid[i][j];
        }
    }
    int pos[2];
    if(grid[r][c]=='d')
        {
        pos[0]=r;
        pos[1]=c;
        
    }
 else if(grid[r-1][c]=='d')
     {
     pos[0]=r-1;
     pos[1]=c;
     
 }
    else if(grid[r-1][c+1]=='d')
     {
     pos[0]=r-1;
     pos[1]=c+1;
     
 }
    else if(grid[r][c+1]=='d')
     {
     pos[0]=r;
     pos[1]=c+1;
     
 }
    else if(grid[r+1][c+1]=='d')
     {
     pos[0]=r+1;
     pos[1]=c+1;
     
 }
    else if(grid[r+1][c]=='d')
     {
     pos[0]=r+1;
     pos[1]=c;
     
 }
    else if(grid[r+1][c-1]=='d')
     {
     pos[0]=r+1;
     pos[1]=c-1;
     
 }
    else if(grid[r][c-1]=='d')
     {
     pos[0]=r;
     pos[1]=c-1;
     
 }
    else if(grid[r-1][c-1]=='d')
     {
     pos[0]=r-1;
     pos[1]=c-1;
     
 }
 else
     {
     if(c<4)
         {
         cout<<"RIGHT";
     }
     else if(r<4)
         {
         cout<<"DOWN";
     }
     else if(r==4 && c==4)
         cout<<"LEFT";
     else if(r==4 && c==0)
         cout<<"RIGHT";
     else if(r==0 && c==4)
         cout<<"DOWN";
     else
         ;
     count++;
 }
   if(count==0)
   {int a=r-pos[0];
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
   }
    return 0;
}
