import java.util.*;
import java.io.*;

public class Main {

    static int t, n;
    static long answer;

    static int[] share; // 일별 주가

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());

		t = Integer.parseInt(st.nextToken());

        for(int i=0; i<t; i++){
            answer = 0;
            sol();
            bw.write(answer + "\n");
        }
        
        bw.flush();
        bw.close();
    }

    public static void sol() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        
        share = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            share[i] = Integer.parseInt(st.nextToken());
        }

        int max = share[n-1]; // 가장 마지막 날의 주가
        for(int i=n-2; i>=0; i--){
            if(max > share[i]){
                answer += max - share[i];
                continue;
            }
            else{
                max = share[i];
            }
        }
        return;
    }
}