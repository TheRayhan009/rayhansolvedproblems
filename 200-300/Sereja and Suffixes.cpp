#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <set>
using namespace std;
int main(){
    // TLE
    int n,m;
    cin>>n>>m;
    deque<int> l;

    for(int j=0;j<n;j++){
        int in;
        cin>>in;
        l.push_back(in);
    }

    // set<int> l_set(l.begin(),l.end());
    // deque<int> x(l_set.begin(),l_set.end());
    
    for(int i=0;i<m;i++){
    int k;
    cin>>k;
    deque<int> x;
    for(int r=k-1;r<n;r++){
        if (find(x.begin(),x.end(),l[r])==x.end()){
            x.push_back(l[r]);
        }
    }
    cout<<x.size()<<endl;
}
 
return 0;
}

// for(int i=0;i<m;i++){
//     int k;
//     cin>>k;
//     deque<int> x;
//     for(int r=k-1;r<n;r++){
//         if (find(x.begin(),x.end(),l[r])==x.end()){
//             x.push_back(l[r]);
//         }
//     }
//     cout<<x.size()<<endl;
// }