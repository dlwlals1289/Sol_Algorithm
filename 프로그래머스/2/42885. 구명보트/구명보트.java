import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int numOfPeople = people.length;
        int answer = 0;
        int index=0;
        boolean[] visited = new boolean[numOfPeople];
        
        Arrays.sort(people);
        
        for(int i=numOfPeople - 1; i>=0; i--){
            if(visited[i]){
                continue;
            }
            else if(people[i] + people[index] <= limit){
                visited[i] = true;
                visited[index] = true;
                index++;
                answer++;
            }
            else{
                answer ++;
                visited[i] = true;
            }
        }
        return answer;
    }
}