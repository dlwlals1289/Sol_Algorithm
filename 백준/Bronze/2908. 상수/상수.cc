// 상수의 수 읽기
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string a, b;
    int sangsuMax;

    cin>>a>>b;
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    
    int aa, bb;
    aa=stoi(a);
    bb=stoi(b);
    sangsuMax=max(aa, bb);

    cout<<sangsuMax;
    
    return 0;
}