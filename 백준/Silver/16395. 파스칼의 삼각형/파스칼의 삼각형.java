import java.util.Scanner;


public class Main{
    static int[][] c=new int[31][31];

    public static int pascal(int a, int b) {
        int x, y;
        for(int i=0;i<=a;i++){
            int min=Math.min(i,b);
            for(int j=0;j<=min;j++){
                if(j==0||j==i)
                    c[i][j]=1;
                else
                    c[i][j]=c[i-1][j-1]+c[i-1][j];
            }
        }
        return c[a-1][b-1];
    }
    public static void main(String[] args){
        int n,k,answer;
        
        Scanner sc=new Scanner(System.in);
        n=sc.nextInt();
        k=sc.nextInt();

        answer=pascal(n,k);
        System.out.println(answer);
    }
}