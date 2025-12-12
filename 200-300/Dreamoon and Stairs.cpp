#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){
    
    int n,m;
    cin>>n>>m;
    deque<int> l;
    deque<int> mals;
    int t=1;
    for(int i=1;i<n;i++){
        int t=i*m;
        mals.push_back(t);
        if (t>=n){
            t=t*(i-1);
            break;
        }
    }
    if(n<m){
        cout<<-1<<endl;
    }else{
        // for(int q:mals){
        //     cout<<q<<endl;
        // }
        if (n%2==0){
             l.assign(n/2,2);
        }else{
            l.assign(n/2,2);
            l.push_back(1);
        }
        for(int j=0;j<mals.size();j++){
            // cout<<l.size()<<endl;
            if (l.size()<=mals[j]){
                cout<<mals[j]<<endl;
                break;
            }
        }
    }
 
return 0;
}