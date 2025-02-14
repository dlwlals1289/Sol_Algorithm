import java.util.*;
import java.io.*;

public class Main {

    static int T;
    static int I;
    static int tx, ty;

    static int[] dx = {-2, -1, 1, 2, 2, 1, -1, -2}; // 1시 방향부터 시계방향 순으로 
    static int[] dy = {1, 2, 2, 1, -1, -2, -2, -1};
    static int[][] visited; // 방문 여부
    static int[][] graph; // 이동한 값

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        T = Integer.parseInt(st.nextToken());
        for (int i=0; i<T; i++){
            st = new StringTokenizer(br.readLine());
            I = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            int kx = Integer.parseInt(st.nextToken()); // 현재 나이트가 있는 행
            int ky = Integer.parseInt(st.nextToken()); // 현재 나이트가 있는 열

            st = new StringTokenizer(br.readLine());
            tx = Integer.parseInt(st.nextToken()); // 나이트가 이동할 행
            ty = Integer.parseInt(st.nextToken()); // 나이트가 이동할 열

            visited = new int[I][I];
            graph = new int[I][I];       
            bfs(kx,ky);
            
            System.out.println(graph[tx][ty]); 
        }      
    }

    public static void bfs(int x, int y){
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{x,y});
        visited[x][y] = 1;

        while(!queue.isEmpty()){
            int[] now = queue.poll();
            int nowX = now[0];
            int nowY = now[1];

            for(int i=0; i<8; i++){
                int nx = nowX + dx[i];
                int ny= nowY + dy[i];
    
                // 나이트가 이동할 곳이 방문하지 않고 체스판 안의 위치이면
                if(0 <= nx && nx < I && 0 <= ny && ny < I && visited[nx][ny] == 0){ 
                    visited[nx][ny] = 1;
                    queue.offer(new int[]{nx, ny});
                    graph[nx][ny] = graph[nowX][nowY]+1;
                }
            }
        }
    }
}