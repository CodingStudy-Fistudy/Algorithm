import java.util.*;
import java.lang.*;
class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int n = triangle.length;
        // 아래서부터 부분 최적값 구하기
        List<Integer>[]list = new ArrayList[n-1];
        for (int i=0;i<n-1;i++){
            list[i] = new ArrayList<>();
        }
        
        for (int i=n-2;i>-1;i--){
            for (int j=0;j<triangle[i].length;j++){
                int mx = Math.max(triangle[i+1][j],triangle[i+1][j+1]);
                triangle[i][j] +=mx;
            
            }
        }
        return triangle[0][0];
    }
}
