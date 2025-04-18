import java.util.*;
class Solution {
    static Map<Character, Character> m = new HashMap<>() {{
            put('(', ')');
            put('{', '}');
            put('[', ']');
        }};
    static int answer = 0;
    Deque<Character> q = new ArrayDeque<>(); 
    
    public int solution(String s) {
        int len = s.length();
            
        for(char c : s.toCharArray()){
            q.add(c);
        }
        q.addFirst(q.pollLast());
        
        for(int i=0; i<len; i++){
            q.add(q.poll()); // 회전
            if(rotate(len)) {
                answer += 1;
            }
        }

        return answer;
    }
    public boolean isValid(char c){
        for(char ch : m.keySet()){
            if(ch == c) return true;
        }
        return false;
    }
    public boolean rotate(int len){
        Stack<Character> stack = new Stack<>();
        int cnt = 0;
        
        for(int j=0; j<len; j++){

            char tmp = q.poll();

            if(isValid(tmp)){ // 여는 괄호이면
                stack.push(tmp);
                cnt += 1;
            }else if(stack.size() != 0 && tmp == m.get(stack.pop())){ // 짝 맞을 때,
                cnt += 1;
            }
            q.add(tmp);
        }
        
        if(cnt == len && stack.isEmpty()) return true;
        return false;
    }
}