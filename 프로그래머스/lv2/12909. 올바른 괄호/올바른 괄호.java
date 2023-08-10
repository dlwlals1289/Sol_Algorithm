import java.util.Stack;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        String[] str = new String[s.length()];
        Stack<Integer> stack = new Stack<>();
        int ans = 0 ;
        for(int i=0; i<s.length(); i++){
            // str[i] = s.substring(i, i+1);
            String tmp = s.substring(i, i+1);
            
            if(tmp.equals("(")){
                ans += 1;
            }
            else{
                if(ans == 0){
                    ans -= 1;
                    answer = false;
                    break;
                }
                else{
                    ans -= 1;
                }
            }
        }
        
        if(ans == 0){
            answer = true;
        }
        else{
            answer = false;
        }
        
        
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        //System.out.println("Hello Java");

        return answer;
    }
}