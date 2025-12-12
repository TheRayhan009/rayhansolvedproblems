#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;
int main(){
    int n,x=0;
    cin>>n;
    for (int i=1;i<=n;i++){
        x=i*(i+1)/2;
        if (x==n){
            cout<<"YES";
            break;
        }else if (x>n){
            cout<<"NO";
            break;
        }
    }
return 0;
}

