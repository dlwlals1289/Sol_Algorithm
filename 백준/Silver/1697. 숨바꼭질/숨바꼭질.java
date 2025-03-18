import java.util.*;
import java.io.*;

public class Main {

    static int n,k;

    static int[] graph;
    static boolean[] visited;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        
        graph = new int[200001];
        visited = new boolean[200001];

        bfs();

        bw.write(graph[k]+ "\n");
        bw.flush();
        bw.close();
    }

    public static void bfs() throws IOException {
        Queue<Integer> q = new LinkedList<>();
        visited[n] = true;
        q.add(n);

        while(! q.isEmpty()){
            int now = q.poll();

            if(0 <= now - 1 && now - 1 <= 200000 && visited[now-1] == false){
                visited[now-1] = true;
                graph[now-1] = graph[now] + 1;
                q.add(now-1);
            }
            if(0 <= now + 1 && now + 1 <= 200000 && visited[now+1] == false){
                visited[now+1] = true;
                graph[now+1] = graph[now] + 1;
                q.add(now+1);
            }
            if(0 <= now*2 && now*2 <= 200000 && visited[now*2] == false){
                visited[now*2] = true;
                graph[now*2] = graph[now] + 1;
                q.add(now*2);
            }
        }
    }
}
