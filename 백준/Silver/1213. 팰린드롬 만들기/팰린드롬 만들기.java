import java.util.*;
import java.io.*;

public class Main {

    static String str;
    static String start = "", end = "";
    static char mid ;
    static String answer;

    static char[] palindrome;
    static int[] alphabet;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

		str = st.nextToken();
        int len = str.length();
        
        alphabet = new int[26];
        palindrome = new char[len];
        
        for(int i=0; i<len; i++){
            char c = str.charAt(i);
            alphabet[c - 'A'] += 1; 
        }

        int odd = 0;
        for(int i=0; i<26; i++){
            int tmp = alphabet[i] / 2;
            int reminder = alphabet[i] % 2;

            if(reminder != 0){
                if(odd != 0){
                    break;
                }
                odd += 1;
                mid = (char)(i+'A');
            }

            for(int j=0; j<tmp; j++){
                start = start + (char)(i+'A');
                end = (char)(i+'A') + end;
            }
        }

        answer = (mid != 0) ? start + mid + end : start + end;
        answer = (answer.length() == len) ? answer : "I'm Sorry Hansoo";
        
        bw.write(answer + "");
        bw.flush();
        bw.close();
    }
}