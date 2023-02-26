#include <iostream>
using namespace std;

class num
{
public:
    int allnum=-1;
    int firstnum;
    int secnum;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    num n, now;
    int count=0, original;
    cin>>n.allnum;

    original=n.allnum; // 처음 값 복사
    // cout<<now.allnum<<'\n';

    for(;now.allnum!=original; n.allnum=now.allnum, count++){
        n.secnum=n.allnum%10;
        n.firstnum=n.allnum/10; // 십의 자리, 일의 자리 분리

        now.allnum=n.firstnum+n.secnum; // 십의 자리와 일의 자리 더하기

        now.secnum=now.allnum%10;
        now.firstnum=now.allnum/10; 

        now.allnum=n.secnum*10+now.secnum;
    }

    cout<<count<<'\n';
    return 0;
}