import java.util.*;
import java.io.*;

public class Main{
    static int n,m;
    static int answer;

    static int [][] arr;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n][m];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();

            for(int j=0; j<m; j++){
                arr[i][j] = str.charAt(j) - '0';
            }

        }

        for(int i=0; i<n; i++){ // row
            for(int j=0; j<m; j++){ // col
                int tmp = arr[i][j];

                for(int k = m-1; k>=j; k--){ // col
                    if(arr[i][k] == tmp){
                        int length = k-j;
                        if(i+length < n && arr[i+length][j] == tmp && arr[i+length][k] == tmp){
                            int size = (length+1) * (length+1); // 각 원소는 한 변의 길이가 1인 정사각형이므로
                            answer = (answer < size) ? size : answer;
                            break;
                        }
                    }
                }

            }
        }

        System.out.println(answer);  
    }
}