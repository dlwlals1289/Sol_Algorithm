// 수 정렬하기 
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n, a;
    vector<int> num;
    cin>>n;

    for (int i = 0; i < n; i++)
    {
        cin>>a;
        num.push_back(a);
    }

    sort(num.begin(), num.end());

    for (int i = 0; i < n; i++)
    {
        cout<<num[i]<<'\n';
    }
    

    return 0;
}