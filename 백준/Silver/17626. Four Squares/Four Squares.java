import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int n;

	static int[] dp;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int sqrt = (int) Math.sqrt(n);

		dp = new int[n+1];
        dp[1] = 1;
		
        for(int i=2; i<=n; i++){
            dp[i] = dp[i-1];
            dp(i);
        }
		System.out.println(dp[n]);
        
    }

    public static void dp(int num){
        int sqrt = (int) Math.sqrt(num);

        for(int i=1; i<= sqrt; i++){
            dp[num] = (int) Math.min(dp[num - i*i], dp[num]);
        }

        dp[num] += 1;
    }
}