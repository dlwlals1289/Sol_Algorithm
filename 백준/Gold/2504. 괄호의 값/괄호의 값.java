import java.util.*;
import java.io.*;

public class Main {

    static String str;
    static int answer;

    static Stack<Character> stack;
    static Stack<Integer> score;
    
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        // StringTokenizer st = new StringTokenizer(br.readLine());
        
        str = br.readLine();
        stack = new Stack<>();
        score = new Stack<>();
        for(int i=0; i<str.length(); i++){
            char c = str.charAt(i);

            if(c == '(' || c == '['){
                stack.push(c);
                score.push(0);
            }
            else if(c == ')' && !stack.isEmpty() && stack.pop() == '('){
                int nScore = score.pop();
                int tmp = (nScore != 0) ? nScore * 2 : 2;
                if(stack.isEmpty()){
                    answer += tmp;
                    continue;
                }
                score.set(stack.size()-1, score.peek() + tmp);
            }
            else if(c == ']' && !stack.isEmpty() && stack.pop() == '['){
                int nScore = score.pop();
                int tmp = (nScore != 0) ? nScore * 3 : 3;
                if(stack.isEmpty()){
                    answer += tmp;
                    continue;
                }
                score.set(stack.size()-1, score.peek() + tmp);
            }
            else{
                answer = 0;
                break;
            }

        }

        if(!stack.isEmpty() || !score.isEmpty()){
            answer = 0;
        }

        bw.write(answer + "\n");
        bw.flush();
        bw.close();
    }
}