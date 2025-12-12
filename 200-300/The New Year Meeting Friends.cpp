#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;
int main(){
    deque<int> l;

    for(int in=0;in<3;in++){
        int a;
        cin>>a;
        l.push_back(a);
    }

    sort(l.begin(),l.end());
    
    cout<<(l[1]-l[0])+(l[2]-l[1]);


return 0;
}