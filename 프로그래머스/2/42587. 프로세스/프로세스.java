import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<int[]> q = new LinkedList<>();
        
        for(int i=0; i<priorities.length; i++){
            // System.out.println(Arrays.toString(new int[]{priorities[i], i}));
            q.add(new int[]{priorities[i], i});
        }
        
        int max = Arrays.stream(priorities).max().getAsInt();
        
        while(true){
            max = Arrays.stream(priorities).max().getAsInt();
            int[] tmp = q.poll();
            
            if(tmp[0] == max){
                answer += 1;
                int idx = Arrays.stream(priorities)
                    .boxed()
                    .collect(Collectors.toList())
                    .indexOf(max);
                priorities[idx] = -1;
                if(tmp[1] == location){
                    break;
                }
            }else{
                q.add(tmp);
            }
        }
        
        // System.out.println(q);
        
        // System.out.println(idx);
        return answer;
    }
}