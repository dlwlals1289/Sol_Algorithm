import java.util.*;
import java.io.*;

public class Main {

    static int n;

    static char[][] graph;
    static boolean[][] visited;
    static int colorB, nonColorB; // 적록색약인 사람이 본 구역의 수, 적록색약이 아닌 사람이 본 구역의 개수

    static int[] dx = {1, 0, -1, 0}; // 우상좌하
    static int[] dy = {0, -1 ,0, 1};

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        
        graph = new char[n][n];
        visited = new boolean[n][n];

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();

            for(int j=0; j<n; j++){
                graph[i][j] = str.charAt(j);
            }
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(visited[i][j] == false){
                    visited[i][j] = true;
                    dfs(j,i,graph[i][j]);
                    nonColorB ++;
                }
            }
        }

        visited = new boolean[n][n]; // 방문 여부 초기화
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(visited[i][j] == false){
                    visited[i][j] = true;
                    dfs(j,i,graph[i][j]);
                    colorB ++;
                }
            }
        }
        bw.write(nonColorB + " " + colorB + "\n");
        bw.flush();
        bw.close();
    }

    public static void dfs(int x, int y, char color) throws IOException {
        // 초록 구역일 경우 빨간 구역으로 초기화
        graph[y][x] = (graph[y][x] == 'G') ? 'R' : graph[y][x];

        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 범위 안이고, 방문하지 않으면
            if(0<= nx && nx < n && 0 <= ny && ny <n && visited[ny][nx] == false){ 
                // 같은 색이면
                if(graph[ny][nx] == color){
                    visited[ny][nx] = true;
                    dfs(nx, ny, color);
                }
            }
        }
    }
}
