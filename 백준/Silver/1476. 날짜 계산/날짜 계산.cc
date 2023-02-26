// 날짜 계산
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int E,S,M;
    cin>>E>>S>>M;

    while (E!=S || S!=M || E!=M)
    {
        int minNum=min({E,S,M});
        if (minNum == E)
        {
            E+=15;
        }
        else if (minNum == S)
        {
            S+=28;
        }
        else
        {
            M+=19;
        }
    }
    cout<<E<<'\n';

    return 0;
}