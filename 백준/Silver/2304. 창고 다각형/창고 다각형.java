import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.io.*;

public class Main {

    static int n,k;
    static int minIndex = Integer.MAX_VALUE, maxIndex = Integer.MIN_VALUE;
    static int answer;

    static int[] ceiling;

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        
        ceiling = new int[1001];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());

            ceiling[l] = h;
            minIndex = Math.min(minIndex, l);
            maxIndex = Math.max(maxIndex, l);
        }
        
        int maxHeight = Arrays.stream(ceiling).max().getAsInt();        
        int idxOfMax = IntStream.range(0, ceiling.length)
        .filter(i -> ceiling[i] == maxHeight)
        .findFirst()
        .orElse(-1);
        
        int index = minIndex;
        int height = ceiling[index];
        for(int i=minIndex; i<=idxOfMax; i++){
            if(ceiling[i] != 0 && ceiling[i] > height){
                answer += (i - index) * height;
                index = i;
                height = ceiling[i];
            }
        }
        
        index = maxIndex;
        height = ceiling[index];
        for(int i=maxIndex; i>=idxOfMax; i--){
            if(ceiling[i] != 0 && ceiling[i] >= height){
                answer += (index - i) * height;
                index = i;
                height = ceiling[i];
            }
        }
        answer += maxHeight;
        

        bw.write(answer+ "\n");
        bw.flush();
        bw.close();
    }
}
