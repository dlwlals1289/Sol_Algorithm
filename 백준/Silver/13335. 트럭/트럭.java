import java.util.*;
import java.io.*;

public class Main {

    static int n,w,L;
    static int answer;

    static Queue<Integer> truck;
    static Queue<Integer> bridge;

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());

        truck = new LinkedList<>();
        bridge = new LinkedList<>();
        st = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++){
            truck.add(Integer.parseInt(st.nextToken()));
        }
        for(int i=0; i<w; i++){
            bridge.add(0);
        }

        sol();
        
        bw.write(answer + "");
        bw.flush();
        bw.close();
    }

    public static void sol(){
        int weight = 0;

		while (!bridge.isEmpty()) {
			answer += 1;
			weight -= bridge.poll();
			
			//모든 트럭이 다리 위를 지나갈 경우
			if(truck.isEmpty()) {
				continue;
			}
			
			// (현재 다리의 하중 + 다음 트럭의 무게) <= 최대하중일 경우
			if (weight + truck.peek() <= L) {
				int tmp = truck.poll();
				weight += tmp;
				bridge.add(tmp);
			}
            else {
				// 다음 트럭이 다리 위로 올라올 수 없는 경우
				bridge.add(0);
			}
		}
    }
}