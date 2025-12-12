#include <iostream>
#include <string>
#include <deque>
#include <algorithm>

using namespace std;
int main(){

    int x,a,b,c_even=0,c_odd=0;
    bool check=false;
    cin>>x;
    for(int i=0;i<x;i++){
        deque<int> l;
        check=false;
        c_even=0;
        c_odd=0;
        cin>>a>>b;
        for (int in=0;in<a;in++){
            int c;
            cin>>c;
            l.push_back(c);
        }

        if (b==1){
            for (int in=0;in<a;in++){
                if (l[in]%2!=0){
                    check=true;
                    break;
                }
            }
        }else{
            for (int in=0;in<a;in++){
                if (l[in]%2==0){
                    c_even+=1;
                }else{
                    c_odd+=1;
                }
            }
            //cout<<c_even<<endl<<c_odd<<endl;
            for (int v=1;v<c_odd+1;v+=2){
                if (abs(b-v) <= c_even ){
                    check=true;
                    break;
                }
            }
        }

        if (check){
            cout<<"Yes"<<endl;
        }else{
            cout<<"No"<<endl;
        }
        l.clear();

    }

    return 0;
}