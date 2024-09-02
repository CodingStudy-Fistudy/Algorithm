import java.util.*;
class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        Deque<Node> dq = new ArrayDeque();
        dq.add(new Node(numbers[0],0));
        dq.add(new Node(-1*numbers[0],0));
        
        while(!dq.isEmpty()){
            Node p = dq.poll();
            if (p.depth+1==numbers.length){
                if (p.num==target){
                    answer++;
                }
                continue;
            }
            dq.add(new Node(p.num+numbers[p.depth+1],p.depth+1));
            dq.add(new Node(p.num-numbers[p.depth+1],p.depth+1));
        }
        
        return answer;
    }
}
class Node{
    int num;
    int depth;
    public Node(int num,int depth){
        this.num = num;
        this.depth = depth;
    }
}

---
저는 파이썬 말고 그냥 하던대로 자바로 풀려구요 ㅎㅎ 순열조합 안나오는 기도메타로 가겠습니다..,,
