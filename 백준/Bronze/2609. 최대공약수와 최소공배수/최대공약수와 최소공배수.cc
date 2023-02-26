// 최대공약수 최소공배수
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n[2];
    int gcd=0, lcm=0;

    for (int i = 0; i < 2; i++)
    {
        cin>>n[i];
    }
    sort(n,n+2);

    for (int i = 1; i < n[0]+1; i++) // 최대공약수 구하기
    {
        if(n[0]%i==0 && n[1]%i==0){
            gcd=i;
        }
    }

    lcm=n[0];
    for (int j = 1; lcm%n[1]!=0; j++) // 최소공배수 구하기
    {
        lcm=j*n[0];
    }
    cout<<gcd<<'\n'<<lcm<<'\n';

    return 0;
}