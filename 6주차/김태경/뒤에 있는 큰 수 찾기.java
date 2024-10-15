import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        
        int[] nums=numbers.clone();
        int len=numbers.length;
        int[] answer=new int[len];
        ArrayDeque<int[]> stack = new ArrayDeque<>();

        stack.push(new int[]{0,numbers[0]});
        for(int i=1;i<len;i++){
            int now = numbers[i];
            if(stack.peek()[1]<now){
                int[] num = stack.pop();
                while(num[1]<now){
                    answer[num[0]]=now;
                    if(stack.isEmpty() || stack.peek()[1]>=now){
                        break;
                    }
                    num = stack.pop();
                }
            }
            stack.push(new int[]{i,numbers[i]});
            
        }
        for(int[] num : stack){
            answer[num[0]] = -1;
        }
        
        return answer;
    }
}
