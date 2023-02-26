// 오븐 시계
#include <iostream>
using namespace std;

int main(){
    int hour, minute;
    int needTime;

    cin>>hour>>minute;
    cin>>needTime;

    minute+=needTime;
    while(minute>=60){
        minute=minute-60;
        hour+=1;
    }
    if(hour>=24){
        hour=hour-24;
    }
    cout<<hour<<" "<<minute;
}