import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int sum;

    static int[][] graph;
    static boolean[][] visited;
    static ArrayList<Integer> answer; 

    static int[] dx = {1, 0, -1, 0}; // 우상좌하
    static int[] dy = {0, -1 ,0, 1};

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        
        graph = new int[n][n];
        visited = new boolean[n][n];
        answer = new ArrayList<>();
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();

            for(int j=0; j<n; j++){
                graph[i][j] = Integer.parseInt(str.substring(j, j+1));
            }
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(visited[i][j] == false && graph[i][j] == 1){
                    visited[i][j] = true;
                    sum = 1;
                    dfs(i, j);
                    answer.add(sum);
                }
            }
        }

        Collections.sort(answer);

        bw.write(answer.size() + "\n");
        for(int i=0; i<answer.size(); i++){
            bw.write(answer.get(i) + "\n");
        }
        bw.flush();
        bw.close();
    }

    public static void dfs(int x, int y) throws IOException {

        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 범위 안이고, 방문하지 않으면
            if(0<= nx && nx < n && 0 <= ny && ny <n && visited[nx][ny] == false){ 
                if(graph[nx][ny] == 1){
                    sum += 1;
                    visited[nx][ny] = true;
                    dfs(nx, ny);
                }
            }
        }
    }
}
