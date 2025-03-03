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
        dp = new long[n+1][3];

        dp[1][0] = dp[1][1] = dp[1][2] = 1;

        for(int i=2; i<n+1; i++){
            dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901;
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901;
            dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901;
        }

        answer = (dp[n][0] + dp[n][1] + dp[n][2]) % 9901;

        bw.write(answer + "");
        bw.flush();
        bw.close();
    }
}