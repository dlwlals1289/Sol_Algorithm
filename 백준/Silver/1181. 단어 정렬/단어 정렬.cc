// 단어 정렬
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool comp(string &s1, string &s2){
    if(s1.size()==s2.size())
        return s1<s2; // 사전적으로 s1이 s2보다 먼저이면 참
    else 
        return s1.size() < s2.size(); // 길이가 더 짧으면 참
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    cin>>n; 
    
    vector <string>v(n);

    for (int i = 0; i < n; i++)
    {
        cin>>v[i]; // 문자열 입력 받기
    }
    
    sort(v.begin(), v.end(), comp); // 사전식으로 정렬
    

    for (int i = 0; i < n; i++)
    {
        if (i!=0&&v[i]==v[i-1]) // 중복되면 출력하지 않고 넘어가기
        {
            continue; 
        }
        
        cout<<v[i]<<'\n'; // 출력
    }
    return 0;
}