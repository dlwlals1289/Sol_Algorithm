// 좌표 정렬하기 2
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool comp(pair<int, int>a, pair<int, int>b){
    if(a.second==b.second){
        return a.first<b.first; // y 좌표 값이 같을 때 앞 vector의 x 좌표 값이 작으면 true
    }
    else{
        return a.second<b.second;
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    cin>>n;

    vector <pair<int, int>>v;
    int a,b;
    for (int i = 0; i < n; i++)
    {
        cin>>a>>b;
        v.push_back(pair<int, int>(a,b));
    }

    sort(v.begin(), v.end(), comp);

    for (int i = 0; i < n; i++)
    {
        cout<<v[i].first<<" "<<v[i].second<<'\n';
    }

    return 0;
}