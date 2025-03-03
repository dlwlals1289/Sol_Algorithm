import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int n;
    static long answer;

    static long[][] dp;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
        dp = new long[n][10];

        for(int i=0; i<10; i++){
            dp[0][i] = 1;
        }

        for(int i=1; i<n; i++){
            for(int j=0; j<10; j++){
                for(int k=0; k<=j; k++){
                    dp[i][j] += dp[i-1][k];
                    dp[i][j] %= 10007;
                }
            }
        }

        for(int i=0; i<10; i++){
            answer += dp[n-1][i];
        }

        answer %= 10007;
        
        bw.write(answer + "");
        bw.flush();
        bw.close();
    }
}