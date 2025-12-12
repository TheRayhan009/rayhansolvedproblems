#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){
    
    int n,a,b,c,countt=0;
    cin>>n>>a>>b>>c;
    deque<int> l;
    l.push_back(a);
    l.push_back(b);
    l.push_back(c);
    sort(l.begin(),l.end());
    int min1=l[0];
    int min2=l[1];
    int min3=l[2];
    while(true){
         if(n>=min1){
            countt+=1;
            n-=min1;
        }
        else if(n==min1){
            countt++;
            n-=min1;
        }
        else if(n>=min2){
            countt+=1;
            n-=min2;
        }
        else if(n==min2){
            countt++;
            n-=min2;
        }
        else if(n>=min3){
            countt+=1;
            n-=min3;
        }
        
        else if(n==min3){
            countt++;
            n-=min3;
        }
        else{
            break;
        }

    }
    //if (countt==1) countt+=1;
    cout<<countt<<endl;

return 0;
}
