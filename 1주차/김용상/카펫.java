import java.lang.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        //감싸는 공식 존재. yellow 기준 1x24 => brown = 54개 .. 반복
        for (int i=1;i<Math.sqrt(yellow)+1;i++){
            if (yellow%i!=0) continue;
            int x = yellow/i;  // 항상 x>=y
            int y = i;
            if (brown==((2*x)+(y*2)+4)){
                return new int[]{x+2,y+2};
            }
        }
        return answer;
    }
}
