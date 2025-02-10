import java.util.*;
import java.io.*;
import java.math.*;


class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        
        Boolean isOdd = ((a+b) % 2 == 0) ? true : false;
        int sum = (a+b);
        
        for(int i = 0; i < (Math.abs(a-b) / 2) + 1; i++){
                answer += sum;
            }
        
        if(isOdd){
            answer -= (sum/2);
        }
        
        return answer;
    }
}