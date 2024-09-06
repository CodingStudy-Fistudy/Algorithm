import java.util.*;
class Solution {
    // 정렬 과정에서 String형태의 두 수(a,b)를 더한 값 a+b 와 b+a를 비교하기
    public String solution(int[] numbers) {
        int n = numbers.length;
        StringBuilder sb = new StringBuilder();
        String [] lst = new String[n];
        for (int i=0;i<n;i++){
            lst[i] = Integer.toString(numbers[i]);
        }
        Arrays.sort(lst,(n1,n2)-> (n2+n1).compareTo(n1+n2));
        
         if (lst[0].equals("0")) {
           return "0";
        }

        for (int i = 0; i < n; i++) {
            sb.append(lst[i]);
        }
        
        return sb.toString();
    }
}
