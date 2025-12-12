#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){
    
    long long int n,m,unit=1;
    cin>>n>>m;
    deque<long long int> l;

    for(int in=0;in<m;in++){
        long long int a;
        cin>>a;
        l.push_back(a);
    }
    for(long int j=0;j<m-1;j++){
        if (l[j]>l[j+1]){
            unit+=1;
        }
    }
    cout<<((unit*n)-(n-l[m-1]))-1<<endl;
return 0;
}
