import java.util.*;
import java.lang.Math;
class Solution {
    private static List<Integer>[] tree;
    private static int MN = 100;
    private static int num ;
    public int solution(int n, int[][] wires) {
        int answer = 0;
        num = n;
        tree = new ArrayList[n+1];
        for (int i=0;i<=n;i++){
            tree[i] = new ArrayList<>();
        }
        for (int[]list:wires){
            tree[list[0]].add(list[1]);
            tree[list[1]].add(list[0]);
        }
        
        for (int i=0;i<wires.length;i++){
            int a = bfs(wires[i][0],wires[i][1]);
            int b = bfs(wires[i][1],wires[i][0]);
            MN = Math.min(Math.abs(a-b),MN);
        }
      
        return MN;
    }

    public int bfs(int a,int b){
        Deque<Integer>dq = new ArrayDeque<>();
        boolean[]visited = new boolean[tree.length];
        int count = 0;
        dq.add(a);
        while(!dq.isEmpty()){
            int poll = dq.poll();
            if (visited[poll])
                continue;
            visited[poll] = true;
            count++;
            for (int k:tree[poll]){
                if (!visited[k]&&k!=b)
                    dq.add(k);
            }
        }
        return count;
    }
}
