class Solution {
    public int solution(long num) {
        int answer = 0;
        
        if(num == 1){
            return 0;
        }
        
        while(answer != 500){
            if(num == 1){
                break;
            }
            else if(num % 2 == 0){ // 짝수라면
                num /= 2;
                answer += 1;
            }
            else{ // 홀수라면
                num = (num*3) + 1;
                answer += 1;
            }
        }
        
        if(answer == 500){
            return -1;
        }
        else{
            return answer;
        }
        
    }
}