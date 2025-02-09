import java.util.*;
import java.io.*;

public class Main {

    static int computer, connect;
    static int answer;

    static ArrayList<Integer>[] graph;
    static int[] visited;
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        computer = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        connect = Integer.parseInt(st.nextToken());

        graph = new ArrayList[computer];
        for(int i=0; i<computer; i++){ // 2차원 ArrayList 
            graph[i] = new ArrayList<Integer>();
        }

        for (int i=0; i<connect; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a-1].add(b-1);
            graph[b-1].add(a-1);
        }

        visited = new int[computer];
        visited[0] = 1;
        dfs(0);
        
        System.out.println(answer);
    }

    public static void dfs(int now){
        int connected = graph[now].size();

        for(int i=0; i<connected; i++){
            int nextNode = graph[now].get(i);
            if (visited[nextNode] == 0){
                answer += 1; // 1번과 연결된 컴퓨터 수 1개 증가
                visited[nextNode] = 1;
                dfs(nextNode);
            }
        }
    }
}