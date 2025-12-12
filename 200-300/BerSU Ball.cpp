#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){
    
    int n,m,l_index=0,r_index=0,counter=0;
    cin>>n;
    deque<int> l;
    for(int i=0;i<n;i++){
        int in;
        cin>>in;
        l.push_back(in);
    }
    cin>>m;
    deque<int> r;
    for(int i=0;i<m;i++){
        int in;
        cin>>in;
        r.push_back(in);
    }

    sort(l.begin(),l.end());
    sort(r.begin(),r.end());

    while(true){
        if (l_index==n || r_index==m){
            break;
        }
        if (abs(l[l_index]-r[r_index]) == 1 || l[l_index]==r[r_index]){
            counter++;
            l_index++;
            r_index++;
        }else{
            if (l[l_index]<r[r_index]){
                l_index++;
            }else{
                r_index++;
            }
        }

    }
    cout<<counter<<endl;
 
return 0;
}