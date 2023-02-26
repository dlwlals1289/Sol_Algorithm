// 그룹 단어 체커
#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n, cnt=0;
    string s;
    cin>>n;

    for (int i = 0; i < n; i++)
    {
        int alpha[26]={0,};

        cin>>s;
        for (int j = 0; j < s.length(); j++)
        {
            if(s[j]!=s[j+1] && alpha[s[j]-'a']!=-1){ // 현재 알파벳이 다음 알파벳과 다르면서 한 번도 사용되지 않은 알파벳이면
                alpha[s[j]-'a']=-1; // 그 알파벳은 더 이상 접근할 수 없도록 한다.
            }
            else if (alpha[s[j]-'a']==-1) // 이미 사용된 알파벳에 접근한다면
            {
                cnt-=1; // cnt에서 1을 빼기 -> 최종적으로 카운트 안 되게 하려고
                break;
            }
        }
        cnt++;
    }
    cout<<cnt<<'\n';
    
    return 0;
}