import java.util.*;
import java.lang.*;
class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        PriorityQueue<Integer>pq = new PriorityQueue<Integer>(Collections.reverseOrder());
        
        //즉 리스트의 max값을 줄여줘야함. 
        for (int work:works){
            pq.add(work);
        }
        while(true){
            int poll = pq.poll();
            if (poll==0) return 0;
            n-=1;
            pq.add(poll-1);
            if (n==0) break;            
        }
        
        while(!pq.isEmpty()){
            int k = pq.poll();
            answer+=(Math.pow(k,2));
        }
        
        return answer;
    }
}
