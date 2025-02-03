import java.util.*;
import java.io.*;

public class Main {

    static int n,k;
    static int answer;
    static int weight;

    static int[] kit;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        kit = new int[n];
        visited = new int[n];
        
        st = new StringTokenizer(br.readLine());
        for(int i =0; i<n; i++){
            kit[i] = Integer.parseInt(st.nextToken());
        }

        answer = 0;
        weight = 500;
        dfs(0);

        System.out.println(answer);
    }

    public static void dfs(int depth){
        if (depth == n){ // 모든 키트를 다 사용해서 운동했다면
            answer += 1;
        }
        else{
            for (int i =0; i<n; i++){
                // 아직 해당 키트를 사용하지 않았고, 키트 사용 후 중량이 500 이상이라면
                if (visited[i] == 0 && (weight + kit[i] - k) >= 500){ 
                    visited[i] = 1; // 사용처리
                    weight = weight + kit[i] - k;
                    dfs(depth+1);
                    weight = weight - kit[i] + k; // 원상복귀
                    visited[i] = 0;
                }
            }
        }
    }
}