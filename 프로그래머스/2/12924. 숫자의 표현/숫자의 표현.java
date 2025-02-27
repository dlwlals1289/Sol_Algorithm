class Solution {
    public int solution(int n) {
        int answer = 0;
        int sum = 0;
        
        for(int i=1; i<n+1; i++){
            for(int j=i; j<n+1; j++){
                sum += j;
            
                if(sum == n){
                    answer += 1;
                    sum = 0;
                    break;
                }
                else if (sum > n){
                    sum = 0;
                    break;
                }
            }
            
        }
        return answer;
    }
}