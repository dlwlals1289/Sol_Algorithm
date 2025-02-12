import java.util.*;
import java.lang.*;

class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        
        String str = Integer.toString(x);
        int len = str.length();
        long sum = 0;
        
        for(int i=0; i<len;i++){
            sum += Integer.parseInt(str.substring(i,i+1));
        }
        
        if(x%sum == 0){
            return true;
        }
        return false;
    }
}