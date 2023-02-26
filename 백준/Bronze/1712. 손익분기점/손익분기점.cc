// 손익분기점
#include <iostream>
using namespace std;

int main(){
    int fixed, variable;
    int cost;

    cin>>fixed>>variable>>cost;

    int sale;
    double sale_d;
    if(cost>variable){
        sale=fixed/(cost-variable);
        sale_d=(double)fixed/(double)(cost-variable);

            cout<<sale+1;
    }
    else{
        cout<<-1;
    }
}