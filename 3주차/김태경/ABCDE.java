import java.io.*;
import java.util.*;
//dfs에 백트레킹
public class Main {
    static ArrayList<Integer>[] graph;  
    static boolean[] visited;  
    static boolean found;  

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken()); 
        int M = Integer.parseInt(st.nextToken()); 

        graph = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            graph[i] = new ArrayList<>();
        }
        //인접리스트
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph[a].add(b);
            graph[b].add(a);  
        }

        visited = new boolean[N];
        found = false;  

        for (int i = 0; i < N; i++) {
            if (!found) {
                dfs(i, 0);  
            }
        }
        // if(found){
        //   System.out.println(1);
        // }else{
        //   System.out.println(0);
        // }
        System.out.println(found ? 1 : 0);
    }

    //깊이 4까지
    static void dfs(int node, int depth) {
        if (depth == 4) {
            found = true;
            return;
        }

        visited[node] = true;
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, depth + 1);  
                if (found) return;  
            }
        }

        visited[node] = false; 
    }
}
