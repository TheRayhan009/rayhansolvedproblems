#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;
int main(){
    string a;
    getline(cin,a);
    if (a[0]=='-'){
        if(int(a[a.size()-1]) > int(a[a.size()-2])){
            a.pop_back();
        }else{
            a.erase(a.size()-2,1);
        }
    }
    int x=stoi(a);
    cout<<x;
return 0;
}