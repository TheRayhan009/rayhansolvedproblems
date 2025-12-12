#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){

    int n,rem=0,sum=0,last_sum=0,m=0;
    string x;
    cin >> n>>x;
    bool z=false;
    for(int i =0;i<n;i++){
        if (x[i] != '7' && x[i] != '4'){
            z=true;
            break;
        }
    }
    if(z){
        cout << "NO";
    }else{
        for(int j =0;j<n/2;j++){
            sum=sum + int(x[j]);
            last_sum = last_sum + int(x[n-j-1]);
        }
        if(sum==last_sum){
            cout << "YES";
        }else{
            cout << "NO";
        }
    }
return 0;
}