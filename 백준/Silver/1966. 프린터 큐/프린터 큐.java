import java.util.*;
import java.io.*;

public class Main {

    static int n,m;
    static int answer;

    static int[] waitingQueue;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(st.nextToken());

        for(int i=0; i<T; i++){
            st = new StringTokenizer(br.readLine());

            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            waitingQueue = new int[n];
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++){
                waitingQueue[j] = Integer.parseInt(st.nextToken());
            }

            answer = 1;
            print();

            bw.write(answer + "\n");
        }
        bw.flush();
        bw.close();
    }

    public static void print(){
        Queue<int[]> q = new LinkedList<>();

        for(int i=0; i<n; i++){ // 첫번째 요소를 고유 위치로, 두번째 요소를 우선순위로
            q.offer(new int[]{i, waitingQueue[i]});
        }

        waitingQueue = Arrays.stream(waitingQueue)
                            .boxed()
                            .sorted(Collections.reverseOrder())
                            .mapToInt(Integer::intValue).toArray();
        for(int i=0; i<n; i++){
            int max = waitingQueue[i];
            
            while(true){
                int[] tmp = q.poll();

                if(tmp[1] == max && tmp[0] == m){ // 남은 출력물 중에 우선순위가 제일 높으면서 원하는 출력물 번호일 경우
                    return;
                }
                else if(tmp[1] == max){ // 남은 출력물 중에 우선순위가 제일 높은 경우
                    answer += 1;
                    break;
                }
                else{
                    q.add(tmp);
                }
            }
        }     
    }
}