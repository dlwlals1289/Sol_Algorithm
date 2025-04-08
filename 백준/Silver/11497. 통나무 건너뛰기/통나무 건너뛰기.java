import java.util.*;
import java.io.*;

public class Main {

    static int t, n;
    static int answer;

    static int[] arr;
    static int[] li;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        t = Integer.parseInt(st.nextToken());

        for(int i=0; i<t; i++){
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());

            arr = new int[n];
            li = new int[n];
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++){
                arr[j] = Integer.parseInt(st.nextToken());
            }

            // 오름차순 정렬
            arr = Arrays.stream(arr)
                        .boxed().sorted()
                        .mapToInt(Integer::intValue).toArray();

            int mid = (arr.length / 2);
            li[mid] = arr[n-1]; // 제일 높은 통나무는 한 가운데에
            int idx = n-2;
            for(int j=1; j<=mid; j++){
                if(0 <= mid - j && idx >=0){
                    li[mid-j] = arr[idx];
                    idx -= 1;
                }
                if(mid + j < n && idx >=0){
                    li[mid+j] = arr[idx];
                    idx -= 1;
                }
            }

            answer = 0;
            for(int j=0; j<n-1; j++){
                int tmp = Math.abs(li[j+1] - li[j]);
                answer = Math.max(tmp, answer);
            }

            System.out.println(answer);
        }
    }
}