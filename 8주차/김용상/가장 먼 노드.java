import java.util.*;
class Solution {
    public int solution(int n, int[][] edge) {
        Deque<Node>dq = new ArrayDeque<>();
        List<Integer>[]graph = new ArrayList[n+1];
        
        boolean[]visited = new boolean[n+1];
        int []cnt = new int[n+1];
        for (int i=0;i<=n;i++){
            graph[i] = new ArrayList<>();
        }
        for (int i=0;i<edge.length;i++){
            graph[edge[i][0]].add(edge[i][1]);
            graph[edge[i][1]].add(edge[i][0]);
        }
        dq.add(new Node(1,0));
        while(!dq.isEmpty()){
            
            Node poll = dq.poll();
            if (visited[poll.num])
                continue;
            visited[poll.num] = true;
            cnt[poll.dep]+=1;
            for (int k:graph[poll.num]){
                if (!visited[k])
                    dq.add(new Node(k,poll.dep+1));
            }
            
        }
        int answer = 0;
        for (int i=2;i<=n;i++){
            if (cnt[i]==0) {
                answer = cnt[i-1];
                break;
            }
        }
        return answer;
    }
}
class Node{
    int num;
    int dep;
    public Node(int num, int dep){
        this.num = num;
        this.dep = dep;
    }
}
