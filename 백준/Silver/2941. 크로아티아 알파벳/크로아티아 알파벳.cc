// 크로아티아 알파벳
#include <iostream>
#include <string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    string s;
    int cnt=0;
    cin>>s;

    for (int i = 0; i < s.length(); i++)
    {
        switch (s[i])
        {
        case 'c': // c=, c-
            if(s[i+1]=='='){
                cnt++;
                i++;
                break;
            }
            else if (s[i+1]=='-')
            {
                cnt++;
                i++;
                break;
            }
            else{
                cnt++;
                break;
            }
            
        case 'd': // dz= d-
            if(s[i+1]=='z' && s[i+2]=='='){
                cnt++;
                i+=2;
                break;
            }
            else if (s[i+1]=='-')
            {
                cnt++;
                i++;
                break;
            }
            else{
                cnt++;
                break;
            }
        case 'l': //lj
            if(s[i+1]=='j'){
                cnt++;
                i++;
                break;
            }
            else{
                cnt++;
                break;
            }
        case 'n': //nj
            if(s[i+1]=='j'){
                cnt++;
                i++;
                break;
            }
            else{
                cnt++;
                break;
            }
        case 's': // s=
            if(s[i+1]=='='){
                cnt++;
                i++;
                break;
            }
            else{
                cnt++;
                break;
            }
        case 'z': // z=
            if(s[i+1]=='='){
                cnt++;
                i++;
                break;
            }
            else{
                cnt++;
                break;
            }
        default :
            cnt++;
        }
    }
    cout<<cnt<<'\n';
    
    return 0;
}