import java.util.*;
import java.io.*;

public class Main {

    static String s,t;
    static int answer;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        // StringTokenizer st = new StringTokenizer(br.readLine());

        s = br.readLine();
        t = br.readLine();
        int len = t.length();

        while(len != s.length()){
            char ch = t.toCharArray()[len-1]; // 현재 문자열의 마지막 문자
            t = t.substring(0,len-1);
            
            if(ch == 'B'){
                StringBuilder sb = new StringBuilder(t);
                t = sb.reverse().toString();
            }

            len = t.length();
            // System.out.println(t);
        }

        answer = (t.equals(s)) ? 1 : 0;
		
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
    }

    public static void sol(String str) throws IOException {

        if(str.length() == t.length()){ // 만들어진 문자열의 길이 ==  정답 문자열의 길이
            if(str.equals(t)){
                answer = 1;
                return;
            }
            else {
                return;
            }
        }
        else {
            StringBuilder sb = new StringBuilder(str);
            sol(str+"A");
            sol(sb.reverse()+"B");
        }
        return;
    }
}