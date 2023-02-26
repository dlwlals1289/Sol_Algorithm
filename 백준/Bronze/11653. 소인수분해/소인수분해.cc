// 소인수분해
#include <iostream>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    cin>>n;

    if (n==1) // n이 1인 경우 아무것도 출력 안 함
    {
        return 0;
    }
    else{
        int num=n;
        for (int i = 2; i < n+1; i++)
        {
            if (num==1) // 소인수분해가 끝나면
            {
                return 0;
            }
            else{
                while(num%i==0 && i<=num){ // num을 i로 더이상 나누어지지 않을 때까지
                    num/=i;
                    cout<<i<<'\n';
                }
            }
        }
    }
    
    return 0;
}