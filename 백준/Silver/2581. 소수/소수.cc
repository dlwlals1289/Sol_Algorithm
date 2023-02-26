// 소수
#include <iostream>
#include <vector>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int m, n;
    int sum=0, minOfPrime;
    vector <int>v;
    int count=0; 
    cin>>m>>n;
    if(m==1){
        m++; // 범위의 최솟값이 1일 경우 1을 포함하지 않도록 m++
    }
    for (int i = m; i < n+1; i++, count=0) // m 이상 n 이하인 정수 i
    {
        for (int j = 2; j < i; j++) // 2부터 i-1까지 
        {
            if(i%j==0){ // i가 j로 나눠지면 -> i가 소수가 아니면
                count++;
                break; // 두번째 for문 탈출
            }
            
        }
        
        if (count == 0) // 소수이면 소수 vector에 넣고 총합에 더하기
        {
            v.push_back(i);
            sum+=i;
        }
    }

    if(v.empty()){
        cout<<"-1";
    }
    else{
        cout<<sum<<'\n';
        cout<<v[0]<<'\n';
    }
    
    return 0;
}