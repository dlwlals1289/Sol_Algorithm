#include <iostream>
using namespace std;

int main(){
    double a,b;
    cin>>a>>b;

    double result;
    result = (double)a/(double)b;
    
    cout.precision(12);
    cout << fixed;
    cout<<result;
}