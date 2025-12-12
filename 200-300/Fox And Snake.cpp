#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){

    int x,m;
    string l;
    cin>>x>>m;
    for(int i=0;i<x;i++){
        if((i+1) % 4 == 0 ){
            cout<<"#";
            for(int in=1;in<m;in++){
                cout<<".";
            }
            cout<<endl;
        }else if((i+1) % 2 == 0 ){
            for(int in=0;in<m-1;in++){
                cout<<".";
            }
            cout<<"#"<<endl;
        }else{
            for(int in=0;in<m;in++){
                cout<<"#";
            }
            cout<<endl;
        }
    }
return 0;
}