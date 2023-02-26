// 셀프 넘버
#include <iostream>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int cons[10001]={0,}; // 생성자 배열
    int num;

    for (int i = 0, j; i < 10001; i++)
    {
        j=i+1;
        num=i+1;
        while(num!=0){
            j+=num%10;
            num/=10;
        }
        if(j<10001) // 배열 범위가 넘어가면 접근하면 안 되므로
            cons[j]++;
    }
   
    for (int i = 1; i < 10001; i++)
    {
        if(cons[i]==0){
            cout<<i<<'\n';
        }
    }

    return 0;
}