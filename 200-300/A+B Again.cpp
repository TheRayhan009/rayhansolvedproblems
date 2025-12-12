#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
using namespace std;
int main(){

    int n;
    cin>>n;
    for (int i=0;i<n;i++){
        int x,y;
        cin>>y;
        x=y;
        int sum=0;
        while (x>0){
            int rem=x%10;
            sum+=rem;
            x=x/10;
        }
        cout<<sum<<endl;

    }

return 0;
}