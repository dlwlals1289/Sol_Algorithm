import java.util.*;
import java.io.*;

public class Main{

    static int n;
    static int answer;

    static char[][] arr;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        arr = new char[n][n];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();

            arr[i] = str.toCharArray();
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(j+1 < n){
                    swap(i, j, i, j+1);
                    sol();
                    swap(i, j, i, j+1);  
                }
                if(i+1 < n){
                    swap(i, j, i+1, j);
                    sol();
                    swap(i, j, i+1, j);
                }
            }
        }

        bw.write(answer + "");
        bw.flush();
        bw.close();
    }

    public static void swap(int x1, int y1, int x2, int y2){
        char tmp = arr[x1][y1];
        arr[x1][y1] = arr[x2][y2];
        arr[x2][y2] = tmp;
    }

    public static void sol(){
        
        for(int i=0; i<n; i++){ // 같은 행
            int r_cnt = 1, c_cnt = 1;
            for(int j=1; j<n; j++){
                if(arr[i][j] == arr[i][j-1]){
                    r_cnt += 1;
                }
                else {
                    answer = Math.max(answer, r_cnt);
                    r_cnt = 1;
                }
    
                if(arr[j][i] == arr[j-1][i]){
                    c_cnt += 1;
                }
                else {
                    answer = Math.max(answer, c_cnt);
                    c_cnt = 1;
                }
            }
            int max = Math.max(c_cnt, r_cnt);
            answer = (answer < max) ? max : answer;
            
        }
    }
}