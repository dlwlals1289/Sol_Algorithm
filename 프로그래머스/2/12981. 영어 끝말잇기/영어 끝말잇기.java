import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        ArrayList<String> used = new ArrayList<>();
        
        char lastChar = words[0].charAt(words[0].length()-1);
        used.add(words[0]);
        
        for(int i = 1; i<words.length; i++){
            char tmp = words[i].charAt(0);
            if(tmp == lastChar && !used.contains(words[i])){
                lastChar = words[i].charAt(words[i].length()-1);
                used.add(words[i]);
            }
            else{
                answer[0] = (i%n) + 1;
                answer[1] = ((i - (i%n)) / n)+1;
                break;
            }
        }

        return answer;
    }
}