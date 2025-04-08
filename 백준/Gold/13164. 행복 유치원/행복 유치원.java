import java.util.*;
import java.io.*;

public class Main{

    static int n,k;
    static long answer;

    static long[] chd;
    static ArrayList<Long> diff;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        chd = new long[n];
        diff = new ArrayList<>();
        st = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++){
            chd[i] = Long.parseLong(st.nextToken());
        }

        for(int i=0; i<n-1; i++){
            diff.add(chd[i+1] - chd[i]);
        }

        Collections.sort(diff, Collections.reverseOrder());

        for(int i=k-1; i<n-1; i++){
            answer += diff.get(i);
        }
    
        bw.write(answer + "");
        bw.flush();
        bw.close();
    }
}