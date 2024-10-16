import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        int[] answer = new int[2];
        PriorityQueue<Integer>pq1 = new PriorityQueue<Integer>();
        PriorityQueue<Integer>pq2 = new PriorityQueue<Integer>(Collections.reverseOrder());
        
        for(int i=0;i<operations.length;i++){
            String[] s = operations[i].split(" ");
            if (s[0].equals("I")){
                pq1.add(Integer.parseInt(s[1]));
                pq2.add(Integer.parseInt(s[1]));
            }else{
                if (pq1.isEmpty())
                    continue;
                 if (s[1].length()==1){
                     int a = pq2.poll();
                     pq1.remove(a);
                 }else{
                     int b = pq1.poll();
                     pq2.remove(b);
                 }
            }
        }
        if (pq1.size()==0) 
            {
                answer[0] = 0;
                answer[1] = 0;
             }
        else {
                answer[0] = pq2.poll();
                answer[1] = pq1.poll();
             }
            
        return answer;
    }
}
