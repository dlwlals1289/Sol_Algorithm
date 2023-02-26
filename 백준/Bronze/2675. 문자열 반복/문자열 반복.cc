// 문자열 반복
#include <iostream>
#include <string>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int cnt=0, repeat;
    string s;

    cin>>cnt;

    for(int i=0; i<cnt;i++){
        cin>>repeat>>s;
        for(int j=0; j<s.length(); j++){
            for(int k=0; k<repeat; k++){
                cout<<s[j];
            }
        }
        cout<<'\n';
    }
    return 0;
}
