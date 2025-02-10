import java.util.*;
import java.lang.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        
        ArrayList<Long> arr = new ArrayList<>();
        int len = Long.toString(n).length();
        for(int i= 0; i<len; i++){
            long tmp = n % 10;
            n /= 10;
            arr.add(tmp);
        }
        
        Collections.sort(arr, Collections.reverseOrder());
        
        answer = arr.get(0);
        for(int i= 1; i<len; i++){
            answer *= 10;
            answer += arr.get(i);
        }
        
        return answer;
    }
}