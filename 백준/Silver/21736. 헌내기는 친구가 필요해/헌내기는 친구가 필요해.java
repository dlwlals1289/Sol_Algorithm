import java.util.*;
import java.io.*;

public class Main {

    static int n,m;
    static int answer;

    static char[][] school;
    static int[][] visited;
    static int[] dx = {1,0,-1,0}; // 동북서남
    static int[] dy = {0,1,0,-1};
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        school = new char[n][m];
        for (int i=0; i<n; i++){ // 2차원 배열 입력 받기
            st = new StringTokenizer(br.readLine());
            
            String str = st.nextToken().toString();
            for(int j=0; j<m; j++){
                school[i][j] = str.charAt(j);
            }
        }

        visited = new int[n][m];
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(school[i][j] == 'I'){
                    visited[i][j] = 1;
                    dfs(i, j);
                    break;
                }
            }
        }

        if(answer != 0){
            System.out.println(answer);
        }
        else{
            System.out.println("TT");
        }
        
        // for(int i=0; i<n; i++){
        //     System.out.println(Arrays.toString(school[i]));
        // }
        // 
    }

    public static void dfs(int x, int y){
        for(int i=0; i<4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(0<= nx && nx < n && 0<= ny && ny < m && visited[nx][ny] == 0){ // 범위 안에 존재하고 방문하지 않은 곳이라면
                if(school[nx][ny] == 'P'){ // 사람이 있는 경우
                    answer += 1;
                    visited[nx][ny] = 1;
                    dfs(nx, ny);
                }
                else if(school[nx][ny] == 'O'){ // 빈 공간일 경우
                    visited[nx][ny] = 1;
                    dfs(nx, ny);
                }
            }
        }
    }
}