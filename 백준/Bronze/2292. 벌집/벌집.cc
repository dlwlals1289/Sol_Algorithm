// 벌집 
#include <iostream>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int beeHouse, cnt=1, sum=1;

    cin>>beeHouse;

    for(int i=1; sum<beeHouse; i++){
        sum+=6*i;
        cnt++;
    }

    cout<<cnt;
    return 0;
}