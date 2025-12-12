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
        int cou=1;
        while (l.size()<=x){
            if(cou % 10 != 3 && cou % 3 != 0){
                l.push_back(cou);
            }
            cou+=1;
        }
        cout<<l[x-1]<<endl;

        // for (int q : l){
        //     cout<<q<<" ";
        // }
        // cout<<endl;
    }

return 0;
}