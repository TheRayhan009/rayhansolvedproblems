#include <iostream>
using namespace std;

int main() {
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		int a,b,c;
		cin>>a>>b>>c;
	
		int ans = c - ( b-a );
		if(b==ans){
			cout<<"YES"<<endl;
		}
		else if (ans%2==0 && b%2!=0 && b+3<=ans){
			cout<<"YES"<<endl;
		}else if(ans%2!=0 && b%2==0 && b+3<=ans){
			cout<<"YES"<<endl;
		}else{
			cout<<"NO"<<endl;
		}


	}


}