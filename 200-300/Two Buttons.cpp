#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <set>
using namespace std;
int main(){
    
    long long int n,m,btn=0;
    cin>>n>>m;

    if (n>m){
        cout<<n-m<<endl;
    }else{
        if(n==m){
        cout<<btn<<endl;
        }else{
            // if(m%2!=0){
            //     m=m-1;
            //     btn+=1;
            // }
            while (n!=m){
                if(n>m){
                    m+=1;
                    btn+=1;
                }else{
                    if(m%2==0){
                        m/=2;
                        btn+=1;
                    }else{
                        m=m+1;
                        //m/=2;
                        btn+=1;
                    }
                }
            }
            cout<<btn;
        }
    }

return 0;
}
