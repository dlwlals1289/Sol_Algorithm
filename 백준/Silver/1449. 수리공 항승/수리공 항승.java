import java.util.*;
import java.io.*;

public class Main{

    static int n,l;
    static int answer;

    static int[] arr;
    
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());

        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr); // 위치를 오름차순으로 정렬

        double idx = arr[0] - 0.5 + l;
        answer = 1;

        for(int pos : arr){
            if (pos + 0.5 <= idx) { // 이미 테이프가 채워진 곳이라면
                continue;
            }
            idx = pos - 0.5 + l; // 붙인 테이프의 맨 오른쪽 위치 업데이트
            answer += 1; // 테이프 개수 1 증가
        }
        
       bw.write(answer + "");
       bw.flush();
       bw.close();
    }
}