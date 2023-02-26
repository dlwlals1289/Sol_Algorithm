// 덩치
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    cin>>n;

    int wh[n][n];
    int grade[n];

    for (int i = 0; i < n; i++)
    {
       cin>>wh[i][0]>>wh[i][1]; // 몸무게랑 키 입력 받기
       grade[i]=1;
    }

    for (int i = 0; i < n; i++)
    {
       for (int j = 0; j < n; j++)
       {
           if (wh[i][1]>wh[j][1] && wh[i][0]>wh[j][0]) // 키 크고 몸무게 높으면 
           {
               grade[j]++;
           }
       }
       
    }
    
    for (int i = 0; i < n; i++)
    {
        cout<<grade[i]<<" ";
    }
    
    return 0;
}