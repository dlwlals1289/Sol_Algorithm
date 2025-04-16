import java.util.*;

class Solution {
    
    public int solution(int[] elements) {
        int answer = 0;
        Set<Integer> s = new HashSet<>();
        
        int len = elements.length;
        
        for(int i=1; i<len+1; i++){ // i = 자를 길이
            int idx = 0;
            // 1번째 원소부터 i번째 원소까지 자르기
            int[] nums = Arrays.copyOfRange(elements, idx, i);
            // 자른 배열의 총합
            int sum = Arrays.stream(nums).sum();
            s.add(sum);
            
            idx += 1;
            while (idx != 0){
                sum -= elements[idx-1];
                sum += elements[(idx+i-1)%len];
                s.add(sum);
                
                
                idx  = (idx+1)%len;
            }
        }
        
        return s.size();
    }
}