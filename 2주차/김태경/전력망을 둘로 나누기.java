import java.util.*;
class Solution {
    ArrayList<Integer>[] graph;
    boolean visited1[];
    boolean visited2[];
    public int solution(int n, int[][] wires) {
        int answer = 101;
        this.visited1=new boolean[n+1];
        this.visited2=new boolean[n+1];
        this.graph=new ArrayList[n+1];
        for(int i=1;i<n+1;i++){
            graph[i]=new ArrayList<>();
        }
        for(int[] wire : wires){
            int i=wire[0];
            int j=wire[1];
            graph[i].add(j);
            graph[j].add(i);
        }
        for(int i=1;i<n+1;i++){
            for(int j : graph[i]){
                int a = bfs(i,j);
                int b=bfs(j,i);
                //answer=Math.min(Math.abs(a-(n-a)),answer);
                answer=Math.min(Math.abs(a-b),answer);
                //System.out.println(answer+ " a="+a+" b="+b);
                visited1=new boolean[n+1];
                // visited1[j]=false;
                // visited1[i]=false;
            }
        }
        
        
        return answer;
    }
    
    int bfs(int s, int d){
        visited1[s]=true;
        visited1[d]=true;
        int cnt=1;
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        dq.offer(s);
        while(!dq.isEmpty()){
            int now = dq.poll();
            for(int k =0; k<graph[now].size();k++){
                if(!visited1[graph[now].get(k)]){
                    cnt++;
                    visited1[graph[now].get(k)]=true;
                    dq.offer(graph[now].get(k));
                        
                }
            }
            
        }
        return cnt;
    }
}
