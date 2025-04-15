import java.util.*;
import java.lang.Math;

class Solution {
    public int solution(int[] arr) {
        int answer = arr[0];
        
        for(int i=1; i<arr.length; i++){
            answer = getLcd(answer, arr[i]);
        }
        return answer;
    }
    
    public int getLcd(int a, int b){
        int max = Math.max(a,b);
        int gcd=1;
        
        for(int i=max; i>0; i--){
            if(a % i == 0 && b % i == 0){
                gcd = i;
                break;
            }
        }
        return gcd * (a/gcd) * (b/gcd);
    }
}