#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){

    int x,m,rem,y=1,a;
    cin>>x;
    for(int i=0;i<x;i++){
        y=1;
        rem=0;
        cin>>m;
        a=m;
        while(m!=0){
            if(m%10!=0){
                rem++;
            }
            m=m/10;
        }
        cout<<rem<<endl;
        m=a;
        // rem=m%10;
        // m=m/10;
        while (m!=0){
            rem=m%10;
            m=m/10;
            if(rem!=0){
                cout<<rem*y<<" ";
            }
            y=y*10;
        }
        cout<<endl;
    }

return 0;
}

