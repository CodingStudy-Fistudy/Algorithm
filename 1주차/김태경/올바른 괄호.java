// false 조건
// 1. 오른쪽 괄호가 왼쪽보다 많이 나온 순간
// 2. 전체 문자열에서 왼쪽, 오른쪽 괄호수가 다른 경우
import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        ArrayDeque<Character> stack = new ArrayDeque<>();
        int lcnt=0;
        int rcnt=0;
        
        for(int i=s.length()-1; i>=0; i--){
            stack.push(s.charAt(i));
        }
      
        // 1. 오른쪽 괄호가 왼쪽보다 많이 나온 순간
        while(!stack.isEmpty()){
            char unit = stack.pop();
            if(unit=='(') lcnt++;
            else rcnt++;
            if(rcnt>lcnt) return false;
        }
      
        // 2. 전체 문자열에서 왼쪽, 오른쪽 괄호수가 다른 경우
        if(rcnt!=lcnt) return false;
        return true;
    }
}
