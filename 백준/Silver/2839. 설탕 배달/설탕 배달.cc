// 설탕 배달 
#include <iostream>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n, n2, count=0;
    cin>>n; // 배달해야 할 설탕 kg
    int sugar[2]={5,3};

    n2=n; // copy
    
    for(int i=n/sugar[0];i>=0;i--, n2=n){
        for (int j = 0; j < i; j++)
        {
            n2-=sugar[0];
            count++;
        }
        if(n2%3==0){
            count=count+n2/3;
            break;
        }
        else {
            count=0;
        }
        
    }
    if(count!=0){
        cout<<count<<'\n';
    }
    else{
        cout<<-1<<'\n';
    }
    return 0;
}