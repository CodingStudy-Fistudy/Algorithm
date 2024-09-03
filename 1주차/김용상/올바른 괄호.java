import java.util.*;
class Solution {
    boolean solution(String s) {
        
        int n = s.length();
        Stack<Character>st = new Stack<>();
        for (int i=0;i<n;i++){
            if (s.charAt(i)=='(')
                st.push('(');
            else{
                if (st.size()==0) return false;
                st.pop();
            }
        }
        
        if (st.size()==0) return true;
        return false;
    }
}
