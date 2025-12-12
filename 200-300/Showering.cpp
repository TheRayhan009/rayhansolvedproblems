#include <iostream>
#include <string>
#include <deque>
#include <algorithm>

using namespace std;
int main(){

    int x,n,s,m,a,b,prev=0;
    bool check = false;
    cin >> x;
    for(int i=0;i<x;i++){
        check = false;
        prev=0;
        cin>>n>>s>>m;
        for(int j=0;j<n;j++){
            cin>>a>>b;
            
            if (abs(prev-a)>=s){
                check = true;
            }
            prev = b;
        }
        // cout<<b<<endl<<m-b<<endl;
        if (abs(m-b) >= s){
            check = true;
        }
        if (check){
            cout<<"YES"<<endl;
        }else{
            cout<<"NO"<<endl;
        }
    }

    return 0;
}