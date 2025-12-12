#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;
int main(){

    int n=0;
    cin>>n;
    cin.ignore();
    for (int i=0;i<n;i++){
        string l;
        getline(cin,l);
        l.pop_back();
        l.pop_back();
        l.push_back('i');
        cout<<l<<endl;
    }

return 0;
}