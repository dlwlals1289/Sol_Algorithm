import java.util.*;
import java.io.*;

public class Main {

    static int n,m,u,v;
    static int answer;

    static int[] visited;
    static ArrayList<Integer>[] connect;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        visited = new int[n];
        connect = new ArrayList[n];

        for(int i=0; i<n; i++){
            connect[i] = new ArrayList<Integer>();
        }
        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());

            connect[u-1].add(v-1);
            connect[v-1].add(u-1);
        }

        
        for(int i=0; i<n; i++){
            if(visited[i] == 0){
                visited[i] = 1;
                dfs(i);
                answer += 1;
            }
        }

        // System.out.println(answer);
        bw.write(answer + "\n");

        bw.flush();
        bw.close();
        br.close();
    }

    public static void dfs(int node){
        int len = connect[node].size();

        for(int i=0; i<len; i++){
            int nextNode = (int) connect[node].get(i);
            if(visited[nextNode] == 0){
                visited[nextNode] = 1;
                dfs(nextNode);
            }
        }
    }
}