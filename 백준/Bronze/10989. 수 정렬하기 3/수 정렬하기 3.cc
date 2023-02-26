// 수 정렬하기 3
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n, num;
    cin>>n;
    long *arr = new long[10001](); // n개의 배열 동적할당

    for (int i = 0; i < n; i++)
    {
        cin>>num;  // n개의 숫자 입력 받기
        arr[num]++; // 입력 받은 숫자가 몇개인지 세는 용도
    }
    for (int i = 0; i < 10001; i++)
    {
        for (int j = 0; j < arr[i]; j++)
        {
            cout<<i<<'\n';
        }
    }

    delete[] arr;

    return 0;
}