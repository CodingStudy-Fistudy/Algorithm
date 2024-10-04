import java.util.*;
class Solution {
    private boolean [] visited ;
    private int cnt = 0;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n+1];
        Deque<Integer>dq = new ArrayDeque<>();
        List<Integer>[]graph = new ArrayList[n+1];
        for (int i=0;i<n;i++){
            graph[i] = new ArrayList<>();
        }
        for (int i=0;i<computers.length;i++){
            for (int j=0;j<computers[i].length;j++){
                if(computers[i][j]==1&&i!=j){
                    graph[i].add(j);
                    graph[j].add(i);
                }
            }
        }
        for (int i=0;i<n;i++){
            if (visited[i]){
                continue;
            }
            cnt++;
            dq.add(i);
            
            while(!dq.isEmpty()){
                int poll = dq.poll();
                if (visited[poll]){
                    continue;
                }
                visited[poll] = true;
                for (int k: graph[poll]){
                    dq.add(k);
                }
            }
        }
        
        
        
        return cnt;
    }
}

