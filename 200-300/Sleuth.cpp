#include <iostream>
#include <string>
#include <deque>
#include <algorithm>
#include <string>
#include <cctype>
using namespace std;
int main(){

    string l;
    getline(cin,l);

    for(int i=l.length() - 1;i>-1;i--){
        if(isalpha(l[i])){
            if (l[i]=='a'||l[i]=='e'||l[i]=='i'||l[i]=='o'||l[i]=='u'||l[i]=='A'||l[i]=='E'||l[i]=='I'||l[i]=='O'||l[i]=='U'||l[i]=='y'||l[i]=='Y'){
                cout<<"YES";
                break;
            
            }else{
                cout<<"NO";
                break;
            }
    }
}
return 0;
}

