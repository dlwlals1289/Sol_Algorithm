//숫자의 합
#include <iostream>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string number;
    int result=0, numOfnum;

    cin>>numOfnum;
    cin>>number;

    for(char ch : number){
        result+=ch-'0';
    }

    cout<<result;
    return 0;
}