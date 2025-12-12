# // #include <iostream>
# // #include <string>
# // #include <deque>
# // #include <algorithm>
# // #include <string>
# // #include <cctype>
# // using namespace std;
# // int main(){
# //     int n;
# //     cin>>n;
# //     for (int j=0;j<n;j++){
# //         string a;
# //         getline(cin,a);
# //         string ans;
# //         ans+=a[0];
# //         for (int i =0;i<size(a);i++){
# //             if (a[i] == ' '){
# //                 ans+=a[i+1];
# //             }
# //         }
# //         cout<<string(ans)<<endl;
# //     }
# // return 0;
# // }

n=int(input())
for i in range(n):
    s=""
    l=list(map(str, input().split()))
    for j in range(len(l)):
       s+=l[j][0]
    print(s) 