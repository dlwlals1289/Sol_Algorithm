// 단어의 개수
#include <iostream>
#include <string>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string sentence, s;
    string space=" ";
    int count=0;

    getline(cin, sentence);

    if(sentence.empty()){
        cout<<0;
        return 0;
    }
    for (int i = 0; i < sentence.length(); i++)
    {
        if(sentence[i]-' '==0){
            count++;
        }
    }
    if(sentence[0]==' ')
        count--;
    if(sentence[sentence.length()-1]==' ')
        count--;
    cout<<count+1;
    return 0;
}
