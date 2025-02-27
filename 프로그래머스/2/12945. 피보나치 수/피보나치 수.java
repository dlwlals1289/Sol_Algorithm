class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int[] fi = new int[n+1];
        fi[0] = 0; 
        fi[1] = 1;
        
        for(int i=2; i<n+1; i++){
            fi[i] = (fi[i-1] + fi[i-2]) % 1234567;
        }
        
        return fi[n];
    }
}