import java.util.*;

public class Main {
    static int n;
    static int m;

    static int[] visited;
    static int[] arr;
    static int[] answer;
    public static void main(String[] args) throws Exception {

        Scanner scanner = new Scanner(System.in);

        n = scanner.nextInt();
        m = scanner.nextInt();

        arr = new int[n]; // 입력받은 정수 저장 용도
        visited = new int[n]; // 방문 여부 체크 용도
        answer = new int[m]; // 정답 배열 저장 용도

        for (int i = 0; i < n; i++){
            arr[i] = scanner.nextInt();
        }

        Arrays.sort(arr); // 오름차순 정렬

        for(int i = 0; i < n; i++){
            visited[i] = 1; 
            answer[0] = arr[i];
            dfs(1);
            visited[i] = 0;
        }
    }

    public static void dfs(int now){
        if (now == m){
            for(int i=0; i<m;i++){
                System.out.print(answer[i] + " ");
            } 
            System.out.print('\n');
        }
        else{
            for (int i = 0; i < n; i++){
                if (visited[i] == 0){ // 방문하지 않았다면
                    visited[i] = 1;
                    answer[now] = arr[i];
                    dfs(now+1);
                    visited[i] = 0;
                }
            }
        }
        
    }
}