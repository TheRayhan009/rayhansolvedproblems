#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <set>
using namespace std;
int main(){
    
    int n,c=0,have_Z=0,have_O=0,maxe=0;
    cin>>n;
    deque<int> l;
    bool check=true;

    for(int j=0;j<n;j++){
        int in;
        cin>>in;
        l.push_back(in);
    }

    for(int i=0;i<n;i++){
        if (l[i]==0){
            have_Z++;
        }else{
            have_O++;
        }
    }

    for(int x=0;x<n;x++){
        if (l[x]==0){
            int a = have_Z-1;
            int b = have_O;
            int c=abs(a-b);
            if (c>maxe){
                maxe=c;
            }
        }else{
            int a = have_Z;
            int b = have_O-1;
            int c=abs(a-b);
            if (c>maxe){
                maxe=c;
            }
            
        }
    }

return 0;
}
