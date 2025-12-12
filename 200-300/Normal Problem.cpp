#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){

    int x,m;
    string l;
    cin>>x;
    for(int i=0;i<x;i++){
        cin>>l;
        for (int in=l.size()-1;in>-1;in--){
            if(l[in]=='q'){
                cout<<'p';
            }else if(l[in]=='p'){
                cout<<'q';
            }else{
                cout<<l[in];
            }


        }
        cout<<endl;
    
    }


return 0;
}