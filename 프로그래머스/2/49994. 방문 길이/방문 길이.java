import java.util.*;
class Solution {
    public int solution(String dirs) {
        int answer = 0;
        int x = 0;
        int y = 0;
        Set<String> s = new HashSet<>();
        
        Map<Character, int[]> m = new HashMap<>();
        m.put('U', new int[]{0, 1});
        m.put('L', new int[]{-1, 0});
        m.put('D', new int[]{0, -1});
        m.put('R', new int[]{1, 0});
        
        for(char c : dirs.toCharArray()) {
            int[] dir = m.get(c);
            int nx = x+dir[0];
            int ny = y+dir[1];
            
            if(-5 <= nx && nx <= 5 && -5 <= ny && ny <= 5 ){
                switch(c){
                    case 'L':
                        if(!s.contains(c + nx + ny) && !s.contains('R'+x+y)){
                            s.add(c + "" + nx + "" + ny);
                            s.add('R'+""+x+""+y);
                            answer += 1;
                        }
                        break;
                    case 'R':
                        if(!s.contains(c + nx + ny) && !s.contains('L'+x+y)){
                            s.add(c + "" + nx + "" + ny);
                            s.add('L'+""+x+""+y);
                        }
                        break;
                    case 'U':
                        if(!s.contains(c + nx + ny) && !s.contains('D'+x+y)){
                            s.add(c + "" + nx + "" + ny);
                            s.add('D'+""+x+""+y);
                        }
                        break;
                    case 'D':
                        if(!s.contains(c + nx + ny) && !s.contains('U'+x+y)){
                            s.add(c + "" + nx + "" + ny);
                            s.add('U'+""+x+""+y);
                        }
                        break;
                }
                x = nx;
                y = ny;
            }
        }
        answer = s.size() /2;
        return answer;
    }
}