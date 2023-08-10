import java.util.StringTokenizer;

class Solution {
    public String solution(String s) {
        StringTokenizer str = new StringTokenizer(s, " ", true);
        // String[] str = s.split(" ");
        String answer = "";
        
        while(str.hasMoreTokens()){
            String tmp = str.nextToken();
            answer += tmp.substring(0,1).toUpperCase() + tmp.substring(1).toLowerCase();
        }
        // for(int i=0; i < str.length; i++){
        //     answer += str[i].substring(0,1).toUpperCase()+str[i].substring(1).toLowerCase()+ " ";
        // }
        
       // answer = answer.substring(0, (answer.length() - 1));
        
        
        return answer;
    }
}