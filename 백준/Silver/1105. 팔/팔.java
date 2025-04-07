import java.util.*;
import java.io.*;

public class Main {

    static int l, r;
    static int answer;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {

        StringTokenizer st = new StringTokenizer(br.readLine());

        l = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        // 자리수가 다를 시 무조건 8이 가장 적게 들어있는 수에 들어있는 8의 개수는 0개이다.
        if(Integer.toString(l).length() == Integer.toString(r).length()){

            int len = Integer.toString(l).length(); // 자리수 체크용
            for(int i=0; i<len; i++){
                if(Integer.toString(l).charAt(i) == Integer.toString(r).charAt(i)){
                    if(Integer.toString(l).charAt(i) == '8'){
                        answer += 1;
                    }
                }
                else{
                    break;
                }
            }
        }   
        bw.write(answer + "");
        bw.flush();
        bw.close();  
    }
}
