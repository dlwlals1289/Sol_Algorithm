// 영화감독 숌
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n,cnt=0;
    cin>>n;

    for (int i = 0; cnt != n; i++)
    {
        int temp=i;
        while (temp>665)
        {
            if(temp%1000==666){
                cnt++;
                break;
            }
            else{
                temp/=10;
            }
        }
        if(cnt==n){
            cout<<i<<'\n';
            break;
        }
    }
    return 0;
}