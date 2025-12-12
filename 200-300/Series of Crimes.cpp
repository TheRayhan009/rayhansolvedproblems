#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){

    int rows,cols ,ans=0,ans2=0;
    cin>>rows>>cols;

    deque<string> data;

    int x=-1,m=0,a=0,b=0,v=0,z=0,q,w;
    for(int i=0;i<rows;i++){
        a=0;
        m=0;
        x=-1;
        string s;
        cin>>s;
        data.push_back(s);

        for (int j=0;j<s.length();j++){
            if (s[j]=='*'){
                a++;
                if (x!=-1){
                    m=j;
                }else{
                    x=j;
                }
                v=j;
            }
        }
        if (a==1){
            b=i;
            z=v;
        }if (a==2){
            q=x;
            w=m;
        }
    }

    if (q==z){
        ans2=b+1;
        ans=w+1;

    }else{
        ans2=b+1;
        ans=q+1;
    }

    cout<<ans2<<' '<<ans;


return 0;
}

