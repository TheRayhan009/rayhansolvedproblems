#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){
    
    long long int n,divs=2;
    cin>>n;
    //bool check=false;
    deque<long long int> l;
    for(int i=0;i<n;i++){
        long long int in;
        cin>>in;
        l.push_back(in);
    }
    
    for(long long int j : l){
        divs=2;
        for (long long int x=2;x<(j/2)+1;x++){
            if (j%x==0){
                divs++;
            }
            if(divs>3){
                break;
            }
 
        }
        if(divs!=3){
            cout<<"NO"<<endl;
        }else{
            cout<<"YES"<<endl;
        }
    }
 
return 0;
}