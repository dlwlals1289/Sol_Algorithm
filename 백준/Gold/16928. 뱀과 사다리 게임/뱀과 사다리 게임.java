import java.util.*;
import java.io.*;

public class Main {

    static int n,m;
    static int answer;

    static HashMap<Integer, Integer> map;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new HashMap<>();
        for(int i=0; i<n+m; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
            map.put(x,y);
        }

        visited = new boolean[101];
        bfs();

        bw.write(answer + "");
		bw.flush();
		bw.close();
    }

    public static void bfs(){
        Queue<Integer> queue = new LinkedList<>();
        visited[1] = true;
        queue.offer(1);

        while(!queue.isEmpty()){
            answer += 1;
            int qSize = queue.size();

            for(int i=0; i<qSize; i++){
                int now = queue.poll();

                for(int j=1; j<=6; j++){

                    if(now + j == 100) return; // 이동할 칸의 번호가 도착 지점일 경우
                    if(now + j > 100) continue; // 이동할 칸의 번호가 100보다 클 경우
                    if(visited[now+j]) continue; // 이동할 칸을 이미 방문한 경우
                    visited[now+j] = true;

                    if(map.containsKey(now+j)){ // 뱀 또는 사다리가 있는 칸일 경우
                        queue.offer(map.get(now+j));
                    }
                    else{ // 일반 칸일 경우
                        queue.offer(now+j);
                    }
                }
            }
        }
    }
}