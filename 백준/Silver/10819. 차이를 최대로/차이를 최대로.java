import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int n;
    static int answer;

    static int[] arr;
    static int[] visited;
    static int[] save;
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        visited = new int[n];
        save = new int[n];
        dfs(0, 0);

        System.out.println(answer);

    }

    public static void dfs(int depth, int sum){
        if(depth == n && sum > answer){
            answer = sum;
        }
        else{
            for (int i= 0; i< n; i++){
                if(visited[i] == 0 && depth != 0){ // 이미 배열 속 원소가 존재할 경우
                    visited[i] = 1;
                    save[depth] = arr[i];
                    dfs(depth+1, sum + Math.abs(save[depth-1] - save[depth]));
                    save[depth] = 0;
                    visited[i] = 0;
                }
                else if(visited[i] == 0 && depth == 0){ // 처음으로 배열에 넣을 경우
                    visited[i] = 1;
                    save[0] = arr[i];
                    dfs(depth + 1 , 0);
                    save[0] = arr[0];
                    visited[i] = 0;
                }
            }
        }
    }
}