// 숫자의 개수
#include <iostream>
using namespace std;

int main(){
    int a,b,c;
    int count[10]={0,};

    int result;

    cin>>a>>b>>c;
    result=a*b*c;

    int i;
    while(result!=0){
        a=result%10;
        result/=10;
        count[a]++;
    }
    for(int i=0; i<10; i++){
        cout<<count[i]<<endl;
    }
}