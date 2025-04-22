import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        int len = topping.length;
        HashMap<Integer, Integer> m1 = new HashMap<>();
        HashMap<Integer, Integer> m2 = new HashMap<>();
        
        for(int t : topping){
            m2.put(t, m2.getOrDefault(t, 0)+1);
        }
        
       for(int t : topping){
           m1.put(t, m1.getOrDefault(t, 0)+1);
           
           int cnt = m2.get(t);
           if(cnt == 1){
               m2.remove(t);
           }else {
               m2.put(t, cnt-1);
           }
           
           
           if(m1.size() == m2.size()) answer += 1;
        }
        
        
        return answer;
    }
}