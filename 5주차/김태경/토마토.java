import java.io.*;
import java.util.*;

public class Main {
    static int M, N;
    static int[][] map;
    static boolean[][] visited;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};
    static ArrayDeque<int[]> dq = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1) {
                    dq.add(new int[] {i, j});
                    visited[i][j] = true;
                }
            }
        }

        int result = bfs();
        System.out.println(result);
    }

    static int bfs() {
        int days = 0;
        
        while (!dq.isEmpty()) {
            int size = dq.size();
            boolean flag = false;

            for (int i = 0; i < size; i++) {
                int[] current = dq.poll();
                int x = current[0];
                int y = current[1];

                for (int j = 0; j < 4; j++) {
                    int nx = x + dx[j];
                    int ny = y + dy[j];

                    if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny] && map[nx][ny] == 0) {
                        map[nx][ny] = 1;
                        visited[nx][ny] = true;
                        dq.add(new int[] {nx, ny});
                        flag = true;
                    }
                }
            }

            if (flag) days++;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) {
                    return -1; 
                }
            }
        }

        return days;
    }
}
