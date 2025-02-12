import java.util.*;
import java.io.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> tmp = new ArrayList<>();
        
        for(int i=0; i<arr.length; i++){
            if(arr[i]%divisor == 0){
                tmp.add(arr[i]);
            }
        }
        
        if(tmp.size() == 0){
            return new int[]{-1};
        }
        
        int[] answer = new int[tmp.size()];
        Collections.sort(tmp);
        
        for(int i=0; i<tmp.size(); i++){
            answer[i] = tmp.get(i);
        }
        return answer;
    }
}