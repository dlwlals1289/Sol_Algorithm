// 최소공배수
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    cin>>n;

    int result[n];
    for (int i = 0; i < n; i++)
    {
        int a, b;
        cin>>a>>b;
        if (a>b)
        {
            swap(a,b); // a에 더 작은 수가 오도록
        }
        
        for (int j = 1; ; j++)
        {
            if ((a*j)%b==0)
            {
                result[i]=a*j;
                break;
            }
        }
    }
    
    for (int i = 0; i < n; i++)
    {
        cout<<result[i]<<'\n';
    }
    
    return 0;
}