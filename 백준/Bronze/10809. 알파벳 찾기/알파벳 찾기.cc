// 알파벳 찾기
#include <iostream>
#include <string>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string s;
    int alphabet[26];
    fill_n(alphabet, 26, -1);

    cin>>s;
    for(int i=0; i<s.length(); i++){
        if(alphabet[s[i]-'a']==-1)
            alphabet[s[i]-'a']=i;
    }
    for(int j=0; j<26; j++){
        cout<<alphabet[j]<<" ";
    }
    
    return 0;
}