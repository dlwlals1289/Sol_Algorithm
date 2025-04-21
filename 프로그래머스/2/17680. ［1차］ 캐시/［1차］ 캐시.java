import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        List<String> cache = new ArrayList<>();
        
        if(cacheSize == 0) return cities.length * 5;
        for(String city : cities){
            if(cache.contains(city.toUpperCase())){
                answer += 1; 
                int tmp = cache.indexOf(city.toUpperCase());
                cache.remove(tmp);
                cache.add(city.toUpperCase());
            }
            else{
                if(cache.size() != 0 && cache.size() == cacheSize){
                    cache.remove(0);
                }
                answer += 5;
                cache.add(city.toUpperCase());
            }
            // System.out.println(city);
        }
        return answer;
    }
}