// 약수
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int numOfdivisor; // 약수 개수
    cin>>numOfdivisor;

    vector <int>v;
    int result=0, count=0;
    for (int i = 0; i < numOfdivisor; i++)
    {
        int a;
        cin>>a; // 약수들 저장하기
        v.push_back(a);
    }
    sort(v.begin(), v.end()); // 약수들 오름차순 정렬

    int b_div=v.back();

    result = v.front()*v.back();
    cout<<result<<'\n';

    return 0;
}