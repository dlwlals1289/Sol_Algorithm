class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int sum = 0;
        
        for(int i=0; i<absolutes.length; i++){
            if (signs[i]){ // 양수면
                sum += absolutes[i];
            }
            else{
                sum += (-1)*absolutes[i];
            }
        }
        return sum;
    }
}