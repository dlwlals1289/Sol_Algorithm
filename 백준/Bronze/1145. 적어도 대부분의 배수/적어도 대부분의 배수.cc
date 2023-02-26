// 적어도 대부분의 배수
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    vector<int> v;
    int n, result, cnt=0;

    for (int i = 0; i < 5; i++)
    {
        cin>>n;
        v.push_back(n); // 5개 정수 입력 받기
    }

    sort(v.begin(), v.end());

    for (result = v[0]; cnt<3; result++)
    {
        cnt=0;
        for (int j = 0; j < 5; j++)
        {
            if(result%v[j]==0){
                cnt++;
            }
        }
    }
    
    cout<<result-1<<'\n';
        
    return 0;
}
