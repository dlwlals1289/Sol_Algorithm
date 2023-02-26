// 평균은 넘겠지?
#include <iostream>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); //cout.tie(NULL);

    int n; // 테스트 개수
    cin>>n;

    for (int i = 0; i < n; i++)
    {
        int student=0; // 학생 수
        double sum=0, average, count=0, result; 
        cin>>student;

        int *score = new int[student]; // 학생 별 점수

        for (int j = 0; j < student; j++)
        {
            cin>>score[j];
            sum+=score[j];
        }
        
        average=sum/student;
        //cout<<"average is "<<average<<'\n';
        
        for (int k = 0; k < student; k++)
        {
            if(score[k]>average)
                count++;
        }
        result=count/student*100;

        cout<<fixed;
        cout.precision(3);
        cout<<result<<"%"<<'\n';

        delete [] score;
    }
    

    return 0;
}