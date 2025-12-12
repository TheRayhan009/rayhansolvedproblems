#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <set>
using namespace std;
int main(){
    
    long long int n,t,sum=0,ans=0,bookCountT=0;
    deque<long long int> l;
    cin>>n>>t;
    for(int i=0;i<n;i++){
        long long int x;
        cin>>x;
        l.push_back(x);
    }
    int it=0;
    for(int j=0;j<n;j++){
        sum+=l[j];
        if(sum>t){
            sum-=l[it];
            it+=1;
            //bookCountT-=1;
        }else{
            bookCountT+=1;
        }
        ans=max(ans,bookCountT);

    }

    cout<<ans<<endl;

return 0;
}
