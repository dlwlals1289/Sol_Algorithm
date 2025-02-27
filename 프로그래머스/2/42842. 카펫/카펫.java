class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        
        answer = new int[2];
        answer[0] = yellow+2;
        answer[1] = yellow+2;
        
        for(int i=1; i<=yellow/2; i++){
            if(yellow % i == 0){
                int row = i;
                int col = yellow/i;
                
                if(2 * (row + col + 2) == brown){
                    answer[0] = col+2;
                    answer[1] = row+2;
                    break;
                }
            }
        }
        return answer;
    }
}