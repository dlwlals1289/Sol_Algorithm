import java.util.*;
import java.io.*;

public class Main {

    static int n;
    static int max;
    static int min;

    static int[] num;
    static int[] op;
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        num = new int[n];
        op = new int[4];

        st =  new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            num[i] = Integer.parseInt(st.nextToken());
        }

        st =  new StringTokenizer(br.readLine());
        for(int i=0; i<4; i++){
            op[i] = Integer.parseInt(st.nextToken());
        }

        max = Integer.MIN_VALUE;
        min = Integer.MAX_VALUE;
        dfs(num[0], op[0], op[1], op[2], op[3]);

        System.out.println(max);
        System.out.println(min);

    }

    public static void dfs(int value, int plus, int minus, int mul, int div){
        if (plus < 0 || minus < 0 || mul < 0 || div < 0){ // 연산자의 개수가 음수라면
            return;
        }

        int numOfOp = plus + minus + mul + div; // 남은 연산자 개수

        if(numOfOp == 0){ // 연산자 다 썼다면
            max = (value > max) ? value : max; // 그 전의 최댓값보다 현재까지의 계산 값이 더 크다면 변경
            min = (value < min) ? value : min; // 그 전의 최솟값보다 현재까지의 계산 값이 더 작다면 변경
        }
        else {
            dfs(value + num[n - numOfOp], plus - 1, minus, mul, div); // 다음 연산자로 + 사용
            dfs(value - num[n - numOfOp], plus, minus - 1, mul, div); // 다음 연산자로 - 사용
            dfs(value * num[n - numOfOp], plus, minus, mul - 1, div); // 다음 연산자로 x 사용
            dfs(value / num[n - numOfOp], plus, minus, mul, div - 1); // 다음 연산자로 ÷ 사용
        }
    }
}