import java.util.*;

class Solution
{
    public int solution(String s)
    {
        int answer = -1;
        Stack<Character> stack = new Stack<>();

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        // System.out.println("Hello Java");
        
        for(char ch : s.toCharArray()){
            if(!stack.isEmpty() && ch == stack.peek()){
                stack.pop();
                continue;
            }
            stack.add(ch);
        }
        
        if(stack.size() == 0){
            return 1;
        }
        return 0;
    }
}