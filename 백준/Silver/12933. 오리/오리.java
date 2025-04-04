import java.util.*;
import java.io.*;

public class Main{

    static String str;
    static int answer;
    static boolean isDuck; // t -> 오리 울음소리인 경우, f -> 오리 울음소리 아님

    static ArrayList<ArrayList<Integer>> duck; // 배열 원소 하나가 한 마리의 오리 객체

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        str = st.nextToken();
        
        duck = new ArrayList<>();
        for(int i=0; i<str.length(); i++){
            isDuck = false; // 올바른 오리 울음소리인지를 나타냄
            sol(str.charAt(i), i);

            if(isDuck == false){
                break;
            }
        }

        answer = (isDuck) ? duck.size() : -1;
        for (ArrayList<Integer> d : duck) {
            if (d.size() % 5 != 0) {
                answer = -1;
                break;
            }
        }    
        
        bw.write(answer + "");
        bw.flush();
        bw.close();
       
    }

    public static void sol(char c, int idx){
        
        switch (c) {
            case 'q': // 각 오리 객체 속 저장된 울음소리 개수가 5의 배수여야 한다. -> q는 오리 울음소리중 가장 앞에 위치하므로
                boolean flag = false;
                for(int i=0; i<duck.size(); i++){
                    if (duck.get(i).size()%5 == 0) { 
                        duck.get(i).add(idx);
                        flag = true;
                        isDuck = true;
                        break;
                    }
                }
                if (!flag) {
                    
                    ArrayList list = new ArrayList<Integer>();
                    list.add(idx);
                    duck.add(list);
                    isDuck = true;
                }
                break;
            case 'u': // 각 오리 객체 속 저장된 울음소리 개수가 5로 나눈 나머지가 1이여야 한다. -> u는 오리 울음소리중 두번째에 위치하므로
                for(int i=0; i<duck.size(); i++){
                    if (duck.get(i).size()%5 == 1) {
                        duck.get(i).add(idx);
                        isDuck = true;
                        break;
                    }
                }
                break;
            case 'a': // 각 오리 객체 속 저장된 울음소리 개수가 5로 나눈 나머지가 2이여야 한다. -> a는 오리 울음소리중 세번째에 위치하므로
                for(int i=0; i<duck.size(); i++){
                    if (duck.get(i).size()%5 == 2) {
                        duck.get(i).add(idx);
                        isDuck = true;
                        break;
                    }
                }
                break;
            case 'c': // 각 오리 객체 속 저장된 울음소리 개수가 5로 나눈 나머지가 3이여야 한다. -> c는 오리 울음소리중 네번째에 위치하므로
                for(int i=0; i<duck.size(); i++){
                    if (duck.get(i).size()%5 == 3) {
                        duck.get(i).add(idx);
                        isDuck = true;
                        break;
                    }
                }
                
                break;
            case 'k': // 각 오리 객체 속 저장된 울음소리 개수가 5로 나눈 나머지가 4이여야 한다. -> k는 오리 울음소리중 가장 마지막에 위치하므로
                for(int i=0; i<duck.size(); i++){
                    if (duck.get(i).size()%5 == 4) {
                        duck.get(i).add(idx);
                        isDuck = true;
                        break;
                    }
                }
                
                break;
            default:
                break;
        }
    }
}
