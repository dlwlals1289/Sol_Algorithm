import java.util.*;
import java.io.*;

public class Main {

    static String str;
    
    static HashMap<String, Integer> subString;
    
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        // StringTokenizer st = new StringTokenizer(br.readLine());
        
        str = br.readLine();

        subString = new HashMap<>();
        for(int i=1; i<=str.length(); i++){
            for(int j=0; (i + j)<=str.length(); j++){
                String tmp = str.substring(j, i+j);

                if(subString.isEmpty() || !subString.containsKey(tmp)){
                    subString.put(tmp, 1);
                }
            }
        }
        

        bw.write(subString.size() + "\n");
        bw.flush();
        bw.close();
    }
}