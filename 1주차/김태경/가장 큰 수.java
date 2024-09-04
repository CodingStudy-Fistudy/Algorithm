import java.util.*;
//문자열 비교(compareTo)는 자리수별로 비교함.
class Solution {
    public String solution(int[] numbers) {
        
        ArrayList<String> list = new ArrayList<>();
        for (int i : numbers) {
            list.add(String.valueOf(i));
        }
      
      //정렬시, 이어붙인것 중 큰값이 앞으로 오도록 비교
        Collections.sort(list, (s1, s2) -> {
            return (s2 + s1).compareTo(s1 + s2);
        });
      
        StringBuilder sb = new StringBuilder();
        for (String s : list) {
            sb.append(s);
        }

        //처음이 "0"인 경우는 값을 "0"으로
        String answer = sb.toString();
        return answer.charAt(0) == '0' ? "0" : answer;
    }
}
