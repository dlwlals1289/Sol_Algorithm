// 평균
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    cin>>n;
    
    double *score = new double[n+1];
    double maxScore, sum=0;
    
     // 과목 수 입력 받기

    for(int i=0; i<n; i++){ // 점수 입력 받기
        cin >> score[i];
        // cout<<i<<'\n';
    }
    maxScore=*max_element(score, score+n); // 최대 점수 구하기

    for(int i=0; i<n; i++){
        score[i]=score[i]/maxScore*100;
        sum+=score[i];
    }
    cout<<sum/n<<'\n';

    return 0;
}