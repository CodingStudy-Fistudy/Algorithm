import java.util.*;
class Solution {
    ArrayList<Integer>[] graph;
    int n; boolean visited[];
    int[] parent;
    public int solution(int n, int[][] computers) {
        int answer = 0;
        this.n=n;
        visited=new boolean[n];
        graph=new ArrayList[n];
        for(int i=0;i<n;i++){
            graph[i]=new ArrayList<>();
        }
        for(int i=0;i<computers.length;i++){
            for(int j=0;j<computers[0].length;j++){
                if(computers[i][j]==1){
                    graph[i].add(j);
                }
                
                
            }
        }
        parent=new int[n];
        for(int i=0;i<n;i++){
            parent[i]=i;
        }
        for(int i=0;i<n;i++){
            visited[i]=true;
            dfs(i);
            
        }
        // for(int i=0;i<n;i++){
        //     System.out.println(parent[i]);
        // }
        
        HashSet<Integer> set=new HashSet<>();
        for(int i=0;i<n;i++){
            set.add(parent[i]);
        }
        return set.size();
    }
    
    void dfs(int num){
        
        for(int i=0;i<graph[num].size();i++){
            if(!visited[graph[num].get(i)]){
                visited[graph[num].get(i)]=true;
                //System.out.println("now="+parent[graph[num].get(i)]+" par="+parent[num]);
                parent[graph[num].get(i)]=parent[num];
                dfs(graph[num].get(i));
                
                
            }
        }
    }
}
