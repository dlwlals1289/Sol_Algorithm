import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int n;
    static int max, min;

    static int[][] dp1, dp2;
    static int[] maxArray, minArray;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
        dp1 = new int[n][3];
        dp2 = new int[n][3];
        
        for(int i=0; i<n; i++){
            int num;
            st = new StringTokenizer(br.readLine());

            for(int j=0; j<3; j++){
                num = Integer.parseInt(st.nextToken());
                dp1[i][j] = num;
                dp2[i][j] = num;
            }
        }

        for(int i=1; i<n; i++){
            // 제일 왼쪽 요소는 윗 줄의 1, 2번째 요소에서만 접근 가능
            dp1[i][0] = Math.max(dp1[i-1][0], dp1[i-1][1]) + dp1[i][0];
            dp2[i][0] = Math.min(dp2[i-1][0], dp2[i-1][1]) + dp2[i][0];

            // 가운데 요소는 윗 줄의 모든 요소에서 접근가능
            dp1[i][1] = Arrays.stream(dp1[i-1]).max().getAsInt() + dp1[i][1];
            dp2[i][1] = Arrays.stream(dp2[i-1]).min().getAsInt() + dp2[i][1];

            // 제일 오른쪽 요소는 윗 줄의 2, 3번째 요소에서만 접근 가능
            dp1[i][2] = Math.max(dp1[i-1][1], dp1[i-1][2]) + dp1[i][2];
            dp2[i][2] = Math.min(dp2[i-1][1], dp2[i-1][2]) + dp2[i][2];
        }

        
        max = Arrays.stream(dp1[n-1]).max().getAsInt();
        min = Arrays.stream(dp2[n-1]).min().getAsInt();

        bw.write(max + " " + min + "");
        bw.flush();
        bw.close();
    }
}