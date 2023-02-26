// 나이 정렬하기
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool comp(pair<int, string> a, pair<int, string> b){
    return a.first<b.first;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    cin>>n;

    vector <pair<int, string>>v;
    int age;
    string name;

    for (int i = 0; i < n; i++)
    {
        cin>>age>>name;
        v.push_back(make_pair(age,name));
    }
    // cout<<v[1].first<<'\n';

    stable_sort(v.begin(),v.end(), comp);

    for (int i = 0; i < n; i++)
    {
        cout<<v[i].first<<" "<<v[i].second<<'\n';
    }

    return 0;
}