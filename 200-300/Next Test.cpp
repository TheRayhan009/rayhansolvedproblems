#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){

    int n;
    cin>>n;
    deque<int> l;
    for (int i=0;i<n;i++){
        int q;
        cin>>q;
        l.push_back(q);
    }
    cout<<n+1;

return 0;
}