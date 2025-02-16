import java.util.*;
import java.io.*;

class Solution {
    public String solution(String[] seoul) {
        StringBuilder sb = new StringBuilder();
        sb.append("김서방은 ");
        
        for(int i=0; i<seoul.length; i++){
            String str = seoul[i];
            if(str.equals("Kim")){
                sb.append(i);
                sb.append("에 있다");
            }
        }
        return sb.toString();
    }
}