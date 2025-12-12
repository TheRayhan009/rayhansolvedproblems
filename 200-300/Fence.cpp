#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <set>
using namespace std;
int main(){
    
    long long int n,k,sum=10000000000,indexx=0,temp=0,lastsub=0;
    deque<long long int> l;
    cin>>n>>k;

    for(int in=0;in<n;in++){
        long long int x;
        cin>>x;
        l.push_back(x);
    }
    for(long int o=0;o<k;o++){
        temp+=l[o];
    }
    sum = temp;
    indexx=1;

    for(long int i=k;i<n;i++){
        temp=temp - (l[lastsub]);
        temp+=l[i];
        lastsub+=1;
        
        if(temp < sum){
            sum = temp;
            indexx=lastsub+1;
        }
    }
    if(indexx!=0)cout<<indexx<<endl;
    if(indexx==0)cout<<indexx+1<<endl;
return 0;
}
