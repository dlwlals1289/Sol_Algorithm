import java.util.*;
import java.io.*;

public class Main {

    static int t, n;
    static int answer;

    static int[][] rank; // 서류평가

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());

		t = Integer.parseInt(st.nextToken());

        for(int i=0; i<t; i++){
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            rank = new int[n][2];
            
            for(int j=0; j<n; j++){
                st = new StringTokenizer(br.readLine());
                rank[j][0] = Integer.parseInt(st.nextToken());
                rank[j][1] = Integer.parseInt(st.nextToken());
            }
            answer = 1;
            sol();
            bw.write(answer + "\n");
        }
        
        bw.flush();
        bw.close();
    }

    public static void sol() throws IOException {

        Arrays.sort(rank, (doc, inter) -> { // 서류 평가 등급을 기준으로 오름차순 정렬
            return doc[0] - inter[0];
        });

        int interMax = rank[0][1]; // 처음에는 서류 평가 1위의 면접 평가 등급이 기준으로 한다.

        for(int j=1; j<n; j++){
            if(rank[j][1] < interMax){
                answer += 1; // 채용할 신입사원 수 증가
                interMax = rank[j][1];
                continue;
            }
        }

        return;
    }
}