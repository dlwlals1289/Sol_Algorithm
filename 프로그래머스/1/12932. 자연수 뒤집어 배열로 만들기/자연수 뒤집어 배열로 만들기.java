import java.util.*;
import java.lang.*;
import java.io.*;

class Solution {
    public int[] solution(long n) {
        int[] answer = {};
        
        String str = Long.toString(n);
        int len = str.length();
        
        answer = new int[len];
        for(int i=0; i<len; i++){
            answer[i] = Integer.parseInt(str.substring(len - 1 -i, len - i));
        }
        


        return answer;
    }
}