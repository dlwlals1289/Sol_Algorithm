// ox 문제
#include <iostream>
#include <string>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int cnt=0, score=0;
    string ox;

    cin>>cnt; // 테스트 개수 입력 받기
    int result[cnt]; // 결과값 배열
    for(int i=0; i<cnt;i++){
        cin>>ox; // ox 입력 받기
        result[i]=0; // 결과값 배열 초기화
        score=0; // score reset

        for(int j=0; j<ox.length(); j++){ // string 길이 만큼 반복
            if(ox[j]=='O'){
                score++;
                result[i]+=score;
            }
            else if(ox[j]=='X'){
                score=0;
            }
        }
        cout<<result[i]<<'\n';
    }
    return 0;
}