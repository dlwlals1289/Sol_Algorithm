import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int n;
    static int answer;

    static int[] arr;
	static int[] dp;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
        arr = new int[n];
        dp = new int[n];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            dp[i] = 1;
        }
		
        for(int i=0; i<n; i++){
            for(int j=0; j<i; j++){
                if(arr[i] < arr[j]){
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
            answer = Math.max(dp[i], answer);
        }

		// System.out.println(dp[n-1]);
        bw.write(answer + "");
        bw.flush();
        bw.close();
    }
}