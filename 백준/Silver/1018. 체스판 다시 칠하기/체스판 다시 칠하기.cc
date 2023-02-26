// 체크판 다시 칠하기
#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int m,n;
    cin>>m>>n;

    string chess[m][n];
    char s[m][n];
    int numOfChange[50][50]{};
    
    for (int i = 0; i < m; i++) // 체스판 입력받기
    {
        for (int j = 0; j < n; j++)
        {
            cin>>s[i][j];
            chess[i][j]=s[i][j];
        }
    }
    int white=0, black=0; // 체스판 맨 처음이 W인 경우와 B인 경우 중 더 적게 바꾸는 경우를 알아내기 위함
    
    for (int k = 0; k < m-7; k++)
    {
        for (int s = 0; s < n-7; s++)
        {
            for (int i = k; i < k+8; i++) 
            {
                for (int j = s; j < s+8; j++)
                {
                    if((i+j)%2==0){
                        if(chess[i][j]=="B"){ // W여야 하는데 B일 경우 
                            white++;
                        }
                    }
                    else{
                        if(chess[i][j]=="W"){ // B여야 하는데 W일 경우 
                            white++;
                        }
                    }
                }
            }
            for (int i = k; i < k+8; i++) 
            {
                for (int j = s; j < s+8; j++)
                {
                    if((i+j)%2==0){
                        if(chess[i][j]=="W"){ // B여야 하는데 W일 경우
                            black++;
                        }
                    }
                    else{
                        if(chess[i][j]=="B"){ // W여야 하는데 B일 경우 
                            black++;
                        }
                    }
                }
            }
            if(white<black){ 
                numOfChange[k][s]=white;
            }
            else{
                numOfChange[k][s]=black;
            }
            white=0; black=0;
        }
    }
    
    int minChange=numOfChange[0][0];

    for (int i = 0; i < m-7; i++)
    {
        for (int j = 0; j < n-7; j++)
        {
            if (minChange>numOfChange[i][j])
            {
                minChange=numOfChange[i][j];
            }
            
        }
    }
    cout<<minChange<<'\n';
    
    return 0;
}