import java.util.*;
import java.io.*;

public class Main {

    static int n,m,k,x;

    static ArrayList<Integer>[] graph;
    static boolean[] visited;
    static ArrayList<Integer> answer;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n+1];
        visited = new boolean[n+1];
        answer = new ArrayList<>();
        for(int i=0; i<n+1; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
        }

        bfs();

        if(answer.size() == 0){ // 최단거리가 k인 도시가 하나도 존재하지 않으면
            bw.write(-1 + "\n");
        }
        else{
            Collections.sort(answer); // 오름차순으로 정렬

            for(int i=0; i<answer.size(); i++){
                bw.write(answer.get(i) + "\n");
            }
        }

        // bw.write(answer + "\n");
        bw.flush();
        bw.close();
    }

    public static void bfs() throws IOException {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x,0});
        visited[x] = true;

        while(! q.isEmpty()){
            int[] next = q.poll();
            int city = next[0];
            int depth = next[1];

            if(depth == k){
                answer.add(city);
                continue;
            }

            for(int i=0; i<graph[city].size(); i++){
                int nextCity = graph[city].get(i);

                if(visited[nextCity] != true){ // 방문하지 않은 도시라면
                    visited[nextCity] = true;
                    q.add(new int[]{nextCity,depth+1});
                }
            }
        }   
        return;
    }
}