import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int len = progresses.length;
        
        
        int idx = 0;
        int count = 0;
        while(idx != len){
            count = 0;
            for(int i=idx; i<len; i++){
                progresses[i] += speeds[i];
            }
            
            for(int i=idx; i<len; i++){
                if(progresses[i] >= 100){
                    idx = i+1;
                    count += 1;
                }else{
                    break;
                }
            }
            
            if(count != 0) answer.add(count);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}