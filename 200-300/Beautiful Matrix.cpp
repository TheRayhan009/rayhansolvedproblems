#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){

    int x=5,q=0,moves=0,f;
    deque<int> nums;
    for(int inx =0;inx<x;inx++){
        for(int in =0;in<x;in++){
            int n;
            cin>>n;
            nums.push_back(n);
            if (n==1){
                f=inx+1;
        }

        }
        for(int i=0;i<x;i++){
            if (nums[i]==1){
                q=i+1;
            }
        }
        nums.clear();
    }
    // cout<<f<<endl<<q<<endl;
    moves=abs(3-f)+abs(3-q);

    cout<<moves;
    

return 0;
}

