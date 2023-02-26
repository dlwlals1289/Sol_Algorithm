// 명령 프롬프트
#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    string file, file2;
    vector<char> v;
    cin>>n;
    cin>>file;

    for (int i = 0; i < n-1; i++)
    {
        cin>>file2; // 파일명 입력 받기
        for (int j = 0; j < file.size(); j++)
        {
            if(file[j]!=file2[j]){
                file[j]='?';
            }
        }
        
    }
    cout<<file<<'\n';
    return 0;
}