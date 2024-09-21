import java.util.*;
class Solution {
    int[][] dp;
    int[] dx={1,1};
    int[] dy={0,1};
    public int solution(int[][] triangle) {
        dp=new int[triangle.length][triangle[triangle.length-1].length];
        
        run(triangle);
        
        int answer = 0;
        for(int i=0;i<triangle[triangle.length-1].length;i++){
            //System.out.println(dp[triangle.length-1][i]);
            answer=Math.max(answer,dp[triangle.length-1][i]);
        }
        return answer;
    }
    
    void run(int[][] tri){
        dp[0][0]=tri[0][0];
        int i=0;
        int j=0;
        for(int u = 0;u<tri.length;u++)
        while (i<tri.length-1 && j<tri[tri.length-1].length-1){
            for(int k=0; k<2;k++){
                int nx=i+dx[k];
                int ny=j+dy[k];
                
                if(nx>=tri.length || ny>=tri[tri.length-1].length ){
                    continue;
                }
                dp[nx][ny]=Math.max(dp[nx][ny], dp[i][j]+tri[nx][ny]);
                
            }
            if(j==i){
                i++;
                j=0;
            }else{
                j++;
            }
        }
    }
}
