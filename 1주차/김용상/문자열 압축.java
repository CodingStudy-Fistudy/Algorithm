import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0;
        int min = s.length();
        int cnt = 1;
        
        for (int i=1;i<(s.length()/2)+1;i++){
            StringBuilder sb = new StringBuilder();
            String s1 = s.substring(0,i);
            
            for (int k=i;k<=s.length();k+=i){
                int last = k+i;
                if (last>s.length()) last = s.length(); 
                
                String s2 = s.substring(k,last);                
                if (s2.equals(s1)){
                    cnt+=1;
                }else {
                    if (cnt>1) {
                        sb.append(cnt);
                    }
                    sb.append(s1);
                    s1 = s2;
                    cnt = 1;
                }
            }
            sb.append(s1);
            
            min = (min>sb.length())?sb.length():min;
        }
        return min;
    }
}
