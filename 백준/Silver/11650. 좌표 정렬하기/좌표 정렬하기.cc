// 좌표 정렬하기
#include <iostream>
#include <vector> 
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n, a, b;
    cin>>n;
    
    vector <pair<int, int>>v;

    for (int i = 0; i < n; i++)
    {
        cin>>a>>b;
        v.push_back(pair<int, int>(a,b));
    }
    sort(v.begin(), v.end());

    for (int i = 0; i < n; i++)
    {
        cout<<v[i].first<<" "<<v[i].second<<'\n';
    }
    
    
    return 0;
}