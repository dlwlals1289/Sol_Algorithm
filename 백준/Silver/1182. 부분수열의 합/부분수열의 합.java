import java.util.*;
import java.io.*;

public class Main {

    static int n,k;
    static int answer;

    static int[] arr;
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        arr = new int[n];
        for (int i=0 ; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        dfs(0,0);
        
        System.out.println(answer);

    }

    public static void dfs(int idx, int sum){
        if(idx == n){
            return;
        }
        if(sum + arr[idx] == k){
            answer += 1;
        }

        dfs(idx + 1, sum+arr[idx]); // 현재 원소 포함한 부분 배열
        dfs(idx + 1, sum); // 현재 원소 미포함 부분 배열
    }
}