// 다리 놓기
// 조합으로 풀기 --> mCn
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int a;
    cin>>a;
    int result[30][30]={0};

    for (int i = 0; i < a; i++)
    {
        int n,m;
        cin>>n>>m;

        for (int j = 1; j <= m; j++)
        {
            result[1][j]=j;
        }
        for (int j = 2; j <= n; j++)
        {
            for (int k = 2; k <= m; k++)
            {
                result[j][k] = result[j-1][k-1] + result[j][k-1];
            }
            
        }
        cout<<result[n][m]<<'\n';
    }
    
    return 0;
}