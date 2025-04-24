import java.util.*;
class Solution {
    public int solution(String word) {
        int answer = 0;
        int len  = word.length();
        List<Character> vowel = Arrays.asList('A', 'E', 'I', 'O', 'U');
        
        for(int i=0; i<len; i++){
            int tmp = vowel.indexOf(word.charAt(i));
            int cnt = 0;
            
            for(int j=0; j<5 -i; j++){
                cnt += Math.pow(5, j);
            }
            answer += (cnt * tmp + 1);
        }
        
        return answer;
    }
}