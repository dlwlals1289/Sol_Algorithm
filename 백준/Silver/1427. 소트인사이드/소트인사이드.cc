//소트인사이드
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string s;
    vector <int>v;
    cin>>s;

    for(char ch : s){
        v.push_back(ch-'0'); // string인 숫자 문자열을 하나하나 정수형으로 바꾼 뒤 vector에 넣음
    }
    sort(v.rbegin(), v.rend());

    for(int i=0; i<v.size(); i++)
    {
        cout << v[i];
    }

    return 0;
}