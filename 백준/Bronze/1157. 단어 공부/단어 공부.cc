// 단어 공부
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string word;
    int duplication=0; // 단어에서 많이 나온 알파벳이 하나인지 아닌지 구별 용도
    cin>>word;
    vector<int>alphabet(26,0);

    for(char c:word){
        int gap=c-'a';
        //cout<<gap<<'\n';
        if(gap<0){
            gap+=32;
        }
        alphabet.at(gap)++;
    }
    int max_index=max_element(alphabet.begin(), alphabet.end())-alphabet.begin(); // 알파벳 벡터에서 최대값의 인덱스 
    int max_value=*max_element(alphabet.begin(), alphabet.end());

    char ch=max_index+'A'; // 인덱스에서 대문자 알파벳으로 바꾸기
    
    for (vector<int>::iterator iter = alphabet.begin(); iter != alphabet.end() ; iter++)
	{
		if(*iter==max_value){
            duplication++; // 단어에서 최대 개수인 알파벳이 여러개 인지 확인
        }
	}
    if(duplication==1){ // 최대 개수인 알파벳이 한 개이면 그 알파벳 대문자로 출력
        cout<<ch<<'\n'; 
    }
    else{ // 아니면 ? 출력
        cout<<"?"<<'\n';
    }
    return 0;
}