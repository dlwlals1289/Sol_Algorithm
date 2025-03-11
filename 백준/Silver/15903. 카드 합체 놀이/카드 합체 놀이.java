import java.util.*;
import java.io.*;

public class Main {

    static int n,m;
    static long answer;

    static List<Long> cards;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        cards = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            cards.add(Long.parseLong(st.nextToken()));
        }

        for(int i=0; i<m; i++){
            Collections.sort(cards);

            long x = cards.get(0);
            long y = cards.get(1);

            cards.set(0, x + y);
            cards.set(1, x + y);
        }

        answer = cards.stream().mapToLong(value -> Long.valueOf(value)).sum();
		
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
    }

    public static void sol(String str) throws IOException {
        return;
    }
}