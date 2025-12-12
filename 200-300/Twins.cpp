#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){

    int x,sum=0,moves=0,vac=0;
    cin>>x;
    deque<int> nums;
    for(int in =0;in<x;in++){
        int n;
        cin>>n;
        nums.push_back(n);
        sum+=n;
    }
    sort(nums.begin(),nums.end());
    for (int i=x-1;i>-1;i--){
        vac+=nums[i];
        moves+=1;
        if (vac>sum-vac){
            break;
        }
    }
    cout<<moves;

return 0;
}

