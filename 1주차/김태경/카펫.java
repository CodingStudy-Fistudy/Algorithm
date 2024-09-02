//가로를 x, 세로를 y라고 했을때 아래 두 방정식을 최적화한다.
// brown = a, yellow = b
// (x-2)(y-2)=a
// xy = a+b
// -> 2x+2y = a;

import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        int totalSum = brown+yellow;
        ArrayList<int[]> array = new ArrayList<>();
        chck(totalSum, array);
        answer = find(brown, array);
        return answer;
    }
    
    //brown+yellow의 약수를 찾아 저장
    public void chck(int totalSum, ArrayList<int[]> array){
        for(int i=1;i<=Math.sqrt(totalSum);i++){
            if(totalSum%i==0){//약수
                array.add(new int[]{totalSum/i,i});
            }
        }
    }
    
    //값 후보인 pair 중 식을 만족하는 값 찾기
    public int[] find(int brown,ArrayList<int[]> array){
        for(int[] pair : array){
            //2x+2y-4 = brown 식을 만족하는 pair찾기
            int value = 2*pair[0] + 2*pair[1] - 4;
            if(value==brown){
                return pair;
            }
        }
        return new int[]{0,0};
        
        
    }
    
}
