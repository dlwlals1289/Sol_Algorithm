import java.util.*;
import java.io.*;

public class Main {

    static int n,m;
    static int x,y;
    static long answer;
    static boolean check; // x에서 시작해서 y까지 도달했는지 여부

    static ArrayList<Integer>[] graph;
    static boolean[] visited;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        graph = new ArrayList[n+1];
        visited = new boolean[n+1];
        for(int i=0; i<n+1; i++){
            graph[i] = new ArrayList<>();
        }

        st = new StringTokenizer(br.readLine());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph[p].add(c);
            graph[c].add(p);
        }

        answer = -1;
        visited[x] = true;
        dfs(x, 0);

        bw.write(answer + "\n");
        bw.flush();
        bw.close();
    }

    public static void dfs(int node, int depth) throws IOException {
        if(node == y){
            answer = depth;
            return;
        }

        int len = graph[node].size();
        for(int i=0; i<len; i++){
            int nextNode = graph[node].get(i); // 다음으로 방문해야 할 사람

            if(visited[nextNode] == false){ // 방문 안 한 사람이라면
                visited[nextNode] = true; // 방문 완료
                dfs(nextNode, depth+1);
            }
        }
        return;
    }
}