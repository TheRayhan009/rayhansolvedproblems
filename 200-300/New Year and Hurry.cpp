#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;
int main(){
    

    int n,k,x=0;
    cin>>n>>k;

    k=240-k;

    for(int i=1;i<n+1;i++){
        if((i*5) <= k ){
            k-=(i*5);
            x+=1;
        }else{
            break;
        }
    }
    cout<<x;


return 0;
}