#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;
int main(){
    int n,deff,countt=0;
    cin>>n>>deff;
    deque <int> l;
    for(int i=0;i<n;i++){
        int in;
        cin>>in;
        l.push_back(in);
    }
    
    sort(l.begin(),l.end());
    
    for (int a=0;a<n;a++){
        for (int b=a+1;b<n;b++){
            if (abs(l[a]-l[b]) <= deff){
                countt++;
            }
        }
    }

    cout<<countt*2;
return 0;
}

