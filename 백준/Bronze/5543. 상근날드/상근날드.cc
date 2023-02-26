//상근날드
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int burger1, burger2, burger3;
    int beverage1, beverage2;

    cin>>burger1>>burger2>>burger3;
    cin>>beverage1>>beverage2;

    int mininum;
    mininum=min({burger1, burger2, burger3})+min({beverage1, beverage2})-50;

    cout<<mininum;
}