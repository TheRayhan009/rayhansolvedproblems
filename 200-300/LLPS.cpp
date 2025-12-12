#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){

    string l;
    cin>>l;
    int max_bit=0;
    char max_bit_char;
    for(int i=0;i<l.length();i++){
        if (int(l[i])>max_bit){
            max_bit=int(l[i]);
            max_bit_char=l[i];
        }
    }
    for(int i=0;i<l.length();i++){
        if (l[i]==max_bit_char){
            cout<<l[i];
        }
    }
    cout<<endl;

return 0;
}

