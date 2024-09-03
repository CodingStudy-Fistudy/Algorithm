import java.util.ArrayList;

//find함수를 통해 1단위부터 문자열/2단위까지 압축을 시도함.
class Solution {
    public int solution(String s) {
        int answer = s.length();

      //절반이상으로 나눈다면 문자열길이랑 똑같게 되어 검사할 필요가 없음 -> s.length()/2로 설정
        for (int i = 1; i <= s.length()/2; i++) {
            answer = Math.min(find(s, i), answer);
        }
        return answer;
    }
  
    //압축단위 : i 
    //반환 : 압축된 길이.
    public int find(String s, int i) {
        ArrayList<String> list = new ArrayList<>();
      //i단위만큼 잘라서 list에 넣음.
        for (int j = 0; j < s.length(); j += i) {
            list.add(s.substring(j, Math.min(j + i, s.length())));
        }

      //단위별로 자른 값(ex. "aab","bbc"....)을 압축
        StringBuilder sb = new StringBuilder();
        for (int j = 0; j < list.size(); j++) {
            int cnt = 1;
            while (j + 1 < list.size() && list.get(j).equals(list.get(j + 1))) {
                cnt++;
                j++;
            }
            if (cnt > 1) {
                sb.append(cnt).append(list.get(j));
            } else {
                sb.append(list.get(j));
            }
        }
        //System.out.println(i+" "+sb);
        
        return sb.length();
    }
}
