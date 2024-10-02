import java.util.*;
class Solution {
    HashSet<Integer> set = new HashSet<>();
    ArrayList<Character> list = new ArrayList<>();
    boolean[] visited;
    StringBuilder sb = new StringBuilder();
    int answer = 0;
    public int solution(String numbers) {
        
        visited=new boolean[numbers.length()];
        perm(numbers,0);
        return answer;
    }
    void perm(String n, int depth){
        if(sb.length()>0){
            int num=Integer.parseInt(sb.toString());
            if(!set.contains(num)){
                set.add(num);
                answer+=find(num);
                //System.out.println(num);
            }
        }
        for(int i=0;i<n.length();i++){
            if(!visited[i]){
                visited[i]=true;
                sb.append(n.charAt(i));
                perm(n,depth+1);
                sb.deleteCharAt(sb.length()-1);
                visited[i]=false;
            }
        }
    }
    int find(int num){
        if(num<2){
            return 0;
        }else if(num==2){
            return 1;
        }
        for(int i=2;i<=num/2+1;i++){
            if(num%i==0){
                return 0;
            }
        }
        return 1;
    }
}
