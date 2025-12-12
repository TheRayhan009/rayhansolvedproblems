#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;
int main(){
    int n,firsr_num_index=0,second_num_index=0;
    cin>>n;
    deque <int> l;
    for(int i=0;i<n;i++){
        int in;
        cin>>in;
        l.push_back(in);
    }
    int sub=abs(l[0]-l[n-1]);
    firsr_num_index=0;
    second_num_index=n-1;
    for(int z=0;z<n-1;z++){
        if(abs(l[z]-l[z+1]) < sub){
            sub=abs(l[z]-l[z+1]);
            firsr_num_index=z;
            second_num_index=z+1;
        }
    }
    cout<<firsr_num_index+1<<" "<<second_num_index+1;
return 0;
}

