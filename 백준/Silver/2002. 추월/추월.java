import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.io.*;

public class Main {

    static int n;
    static int answer;

    static ArrayList<String> carsInT; // 터널로 들어간 자동차 순서
    static ArrayList<String> carsOutT; // 터널에서 나온 자동차 순서
    static ArrayList<String> passing; // 추월한 자동차들

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());

        carsInT = new ArrayList<>();
        carsOutT = new ArrayList<>();
        passing = new ArrayList<>();
        for(int i=0; i<n; i++){
            carsInT.add(br.readLine());
        }

        for(int i=0; i<n; i++){
            carsOutT.add(br.readLine());
        }
        
        String pCar = carsInT.get(0);

        while(!carsOutT.isEmpty()){
            pCar = carsInT.get(0);
            if(pCar.equals(carsOutT.get(0))){ // 들어온 차 번호와 나간 차의 번호가 같으면
                carsInT.remove(0);
                
                carsOutT.remove(0);
            }
            else if(passing.contains(pCar)){ // 이미 추월한 차라고 판단된 경우
                carsInT.remove(0);
                
                pCar = carsInT.get(0);
            }
            else{ // 추월한 차일 경우
                passing.add(carsOutT.get(0));
                carsOutT.remove(0);
            }
        }

        bw.write(passing.size()+ "\n");
        bw.flush();
        bw.close();
    }
}