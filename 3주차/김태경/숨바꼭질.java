import java.io.*;
import java.util.*;

public class Main {
    static final int MAX = 100001; 

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        if (N == K) {
            System.out.println(0);
        } else {
            System.out.println(bfs(N, K)); 
        }
    }

    public static int bfs(int N, int K) {
        int[] time = new int[MAX]; 
        boolean[] visited = new boolean[MAX]; 

        ArrayDeque<Integer> dq = new ArrayDeque<>(); 


        dq.offer(N);
        visited[N] = true;

        while (!dq.isEmpty()) {
            int current = dq.poll();

 
            if (current == K) {
                return time[current];
            }

            //순간이동
            if (current * 2 < MAX && !visited[current * 2]) {
                dq.offerFirst(current * 2); 
                visited[current * 2] = true;
                time[current * 2] = time[current];
            }

            //앞쪽
            if (current + 1 < MAX && !visited[current + 1]) {
                dq.offerLast(current + 1); 
                visited[current + 1] = true;
                time[current + 1] = time[current] + 1;
            }

            //뒤쪽 이동시
            if (current - 1 >= 0 && !visited[current - 1]) {
                dq.offerLast(current - 1);
                visited[current - 1] = true;
                time[current - 1] = time[current] + 1;
            }
        }

        return 0;
    }
}
