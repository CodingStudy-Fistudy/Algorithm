//1. bfs 풀이
import java.util.*;
class Solution {
    ArrayList<Integer>[] graph;
    boolean visited1[];
    public int solution(int n, int[][] wires) {
        int answer = 101;
        this.visited1=new boolean[n+1];
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
                answer=Math.min(Math.abs(a-(n-a)),answer);
                //System.out.println(answer+ " a="+a+" b="+b);
                visited1=new boolean[n+1];

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

////////////////////////////////////////////////////////////////////////////
//2. dfs 풀이
import java.util.*;
class Solution {
    int answer=101;
    ArrayList<Integer>[] graph;
    boolean visited[];
    int n;
    public int solution(int n, int[][] wires) {
        this.visited= new boolean[n+1];
        graph = new ArrayList[n+1];
        this.n=n;
        for(int i=1;i<n+1;i++){
            graph[i]=new ArrayList<>();
        }
        for(int i=0;i<wires.length;i++){
            graph[wires[i][0]].add(wires[i][1]);
            graph[wires[i][1]].add(wires[i][0]);
        }
        visited[1]=true;
        dfs(1);
        
        return answer;
    }
    int dfs(int num){
        
        int sum=0;
        for(int i=0;i<graph[num].size();i++){
            if(visited[graph[num].get(i)]){
                continue;
            }
            visited[graph[num].get(i)]=true;
            int value=dfs(graph[num].get(i));
            answer=Math.min(answer,Math.abs(n-2*value));
            sum+=value;
        }
        if(sum==0){
            return 1;
        }
        return sum+1;
    }
}
