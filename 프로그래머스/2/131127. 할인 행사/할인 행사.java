import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        for(int i=0; i< discount.length-9; i++){ //100,000
            String[] sliced = Arrays.copyOfRange(discount, i, i+10);
            List<String> tmp = Arrays.asList(sliced);
            int count = 0;
            for(int j=0; j<want.length; j++){
                String now = want[j];
                int total = (int) tmp.stream().filter(o -> o.equals(now)).count();
                if(total == number[j]){
                    count += total;
                }else{
                    continue;
                }
            }
            
            if(count == 10){
                answer += 1;
            }
        }
        return answer;
    }
}