// 별 찍기2
#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int count;
    cin>>count;

    for(int i=1; i<count+1;i++){
        for(int j=1; j<=count-i; j++){
            cout<<" ";
        }
        for(int k=100-i; k<100; k++){
            cout<<"*";
        }
        cout<<endl;
    }
    
}