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
        int co=0;
        bool p=false;
        string lst;
        getline(cin,lst);
        for(int j=0;j<lst.size()-1;j++){
            if (lst[j]==lst[j+1]){
                p=true;
                break;
            }
        }
        if (p){
            cout<<1<<endl;
        }else{
            cout<<lst.size()<<endl;
        }
    }

return 0;
}