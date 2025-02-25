import java.util.*;
import java.io.*;

public class Main {

    static int n,m,b;
    static int min, max;
    static int time, height;

    static int[][] ground;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        ground = new int[n][m];
        min = 256;
        max = 0;
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++){
                ground[i][j] = Integer.parseInt(st.nextToken());
                min = Integer.min(min, ground[i][j]);
                max = Integer.max(max, ground[i][j]);
            }
        }

        time = Integer.MAX_VALUE;
        for(int i=min; i<max+1; i++){
            sol(i);
        }
        bw.write(time + " " + height + "");
        bw.flush();
        bw.close();
    }

    public static void sol(int h){
        int sum=0;
        int block = b; 

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                int tmp = ground[i][j];

                if(tmp >= h){ // 만약 비교할 땅의 높이보다 해당 땅의 높이가 더 높다면
                    sum += (tmp-h)*2; // 차이의 두배만큼 시간 저장
                    block += (tmp-h); // 차이만큼 인벤토리에 저장
                }
                else{ // 만약 비교할 땅의 높이보다 해당 땅의 높이가 더 낮다면
                    sum += (h-tmp); // 차이만큼 시간 저장
                    block -= (h-tmp); // 차이만큼 인벤토리에서 차감
                }
            }
        }

        if(block >= 0 && sum <= time){ // 가지고 있는 블럭 수가 음수가 아니면서 최단 시간일 경우
            time = sum;
            height = h;
        }
    }
}