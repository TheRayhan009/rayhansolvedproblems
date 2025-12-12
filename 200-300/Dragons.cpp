#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){
    
    long int in_strength,dragons,xi,yi;
    cin>>in_strength>>dragons;
    deque<deque<int>> l;
    bool check=false;
    for (int i=0;i<dragons;i++){
        cin>>xi>>yi;
        l.push_back(deque<int>{xi,yi});
    }
    sort(l.begin(),l.end());
    for(int j=0;j<dragons;j++){
        if (l[j][0] < in_strength){
            in_strength+=l[j][1];
        }else{
            check=true;
        }
    }
    if (check){
        cout<<"NO"<<endl;
    }else{
        cout<<"YES"<<endl;
    }

return 0;
}
