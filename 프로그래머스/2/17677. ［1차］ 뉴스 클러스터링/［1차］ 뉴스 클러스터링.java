import java.util.*;
import java.util.stream.Collectors;
class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        int len1 = str1.length();
        int len2 = str2.length();
        HashMap<String, Integer> m1 = new HashMap<>();
        HashMap<String, Integer> m2 = new HashMap<>();

        for(int i=0; i<len1-1; i++){
            String tmp = str1.substring(i, i+2).toUpperCase();
            
            if(validString(tmp)){ // 공백, 특수문자, 숫자를 포함하지 않는 올바른 문자열일 경우
                m1.put(tmp, m1.getOrDefault(tmp, 0)+1);
            }
        }
        for(int i=0; i<len2-1; i++){
            String tmp = str2.substring(i, i+2).toUpperCase();
            
            if(validString(tmp)){ // 공백, 특수문자, 숫자를 포함하지 않는 올바른 문자열일 경우
                m2.put(tmp, m2.getOrDefault(tmp, 0)+1);
            }
        }
        if(m1.size() == 0 && m2.size()== 0) return 65536;
        int inter = 0;
        int union = 0;
        for(String k : m1.keySet()){
            if(m1.get(k) != null && m2.get(k) != null){
                inter += Math.min(m1.get(k), m2.get(k));
                union += Math.max(m1.get(k), m2.get(k));
            }else {
                union += m1.get(k);
            }
        }
        for(String k : m2.keySet()){
            if(m1.get(k) == null){
                union += m2.get(k);
            }   
        }
        answer = (int)(((double)inter/union)*65536);
        return answer;
    }
    
    public boolean validString(String str){
        boolean hasSpace = str.matches(".*\\s.*");           // 공백
        boolean hasDigit = str.matches(".*\\d.*");           // 숫자
        boolean hasSpecial = str.matches(".*[^a-zA-Z0-9\\s].*"); // 특수문자
        
        return !hasSpace && !hasDigit && !hasSpecial;
    }
}