import java.util.*;
import java.io.*;

public class Main {

    static int n,p;
    static int answer;

    static int[][] arr;
    static ArrayDeque<Integer>[] finger;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());

        arr = new int[n][2];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        finger = new ArrayDeque[7];
        for(int i=1; i<=6; i++){
            finger[i] = new ArrayDeque<>();
        }

        finger[arr[0][0]].add(arr[0][1]); // 제일 처음 누르는 음 deque에 넣기
        answer += 1;
        for(int i=1; i<n; i++){
            int line = arr[i][0];
            int fret = arr[i][1];

            // System.out.println(i + " " + answer);
            // 현재 해당 음의 누르고 있는 프렛이 있고, 그 프랫이 다음 누를 프렛보다 클 경우
            while(!finger[line].isEmpty() && fret < finger[line].peekLast()){
                finger[line].pollLast();
                answer +=1 ;
            }
                
            // 이미 누르고 있는 프렛일 경우
            if(!finger[line].isEmpty() && fret == finger[line].peekLast()){
                continue;
            }
            else{ // 해당 음의 누르고 있는 프렛이 없는 경우 OR 이미 누르고 있는 프렛이 아닐 경우
                finger[line].add(fret);
                answer += 1;
            }
        }
        

        bw.write(answer + "\n");
        bw.flush();
        bw.close();
    }
}

