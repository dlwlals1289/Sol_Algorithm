import java.util.*;
import java.lang.*;

class Solution {
    boolean solution(String s) {
        
        int numOfP = 0;
        int numOfY = 0;
        int len = s.length();
        
        for(int i=0; i<len; i++){
            String tmp = s.substring(i, i+1);
            if(tmp.equals("p") || tmp.equals("P")){
                numOfP += 1;
            }
            else if(tmp.equals("y") || tmp.equals("Y")){
                numOfY += 1;
            }
        }

        if(numOfP == numOfY){
            return true;
        }
        return false;
    }
}