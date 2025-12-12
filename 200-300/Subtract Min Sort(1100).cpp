#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){

    int n;
    cin>>n;
    for (int i=0;i<n;i++){
        int x;
        cin>>x;
        deque<int> l;
        bool check=false;
        for(int in=0;in<x;in++){
            int t;
            cin>>t;
            l.push_back(t);
        }

        for(int q=0;q<x-1;q+=1){
            int z = min(l[q],l[q+1]);
            l[q] = l[q] - z;
            l[q+1] = l[q+1] - z;

            if(l[q]>l[q+1]){
                check=true;
                break;
            }

        }

        if (check){
            cout<<"NO"<<endl;
        }else{
            cout<<"YES"<<endl;
        }
    }

return 0;
}