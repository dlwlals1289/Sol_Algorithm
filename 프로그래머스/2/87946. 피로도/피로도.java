import java.util.*;

class Solution {
    static boolean[] visited;
    
    public int solution(int k, int[][] dungeons) {
        int answer = 0;
        int len = dungeons.length;
        
        visited = new boolean[len];
        for(int i=0; i<len; i++){
            if(dungeons[i][0] <= k){
                visited[i] = true;
                answer = Math.max(dfs(len, 1, dungeons, k-dungeons[i][1]),answer);
                visited[i] = false;
            }
        }
        
        return answer;
    }
    
    public int dfs(int n, int cnt, int[][] arr, int f){
        int max = cnt;
        for(int i=0; i<n; i++){
            if(!visited[i] && arr[i][0] <= f){
                visited[i] = true;
                max = Math.max(dfs(n, cnt + 1, arr, f - arr[i][1]), max);
                visited[i] = false;
            }
        }
        
        return max;
    }
}