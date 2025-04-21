import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        int len = Integer.parseInt(Long.toString(right - left));
        int[] answer = new int[len + 1];
        
        int idx = (int) left % n;
        int row = (int) left / n;
        for(int i=0; i<right - left +1; i++){
            long tmp = left + i ;
            answer[i] = (int) Math.max(tmp/n, tmp%n) + 1;
        }
        // System.out.println(Arrays.toString(answer));
        return answer;
    }
}