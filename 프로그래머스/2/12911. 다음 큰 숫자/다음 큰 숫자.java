import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 0;
        int cnt = count(n);
        
        while(true){
            n += 1;
            if(cnt == count(n)){
                answer = n;
                break;
            }
        }
        return answer;
    }
    
    public int count(int num){
        int cnt=0;
        
        while(num>0){
            if(num % 2 == 1){
                cnt++;
            }
            num /= 2;
        }
        
        return cnt;
    }
}