#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin>>n;
    int stack[100011];
    int top = -1;
    int max;
    for(int i=0;i<n;i++)
    {
        int a,b;
        cin>>a;
        if(a==1)
        {
            cin>>b;
            top++;
            stack[top] = b;
            if(top == 0)
            {
                max = stack[top];
            }
            else
            {
                if(max < stack[top])
                    max = stack[top];
            }
        }
        else if(a==2)
        {
            if(max == stack[top])
            {
                int temp = top-1;
                max = stack[temp];
                while(temp >= 0)
                {
                    if(stack[temp] > max)
                        max = stack[temp];
                    temp--;
                }
            }
            
            top--;
        }
        else
        {
            cout<<max<<endl;
    }
    }
    return 0;
}
