import java.lang.Math;

class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 0;
        int maxRound = 0;
        
        while(n>1){
            n /= 2;
            maxRound += 1;
        }
        
        int div;
        for(int i=0; i<maxRound; i++){
            div = (int)Math.pow(2,i+1);
            if(((a-1)/div) == ((b-1)/div)){
                answer = i+1;
                break;
            }
        }        

        return answer;
    }
}