
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] board  = new int[N+1];
        int[] dp = new int[N+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            board[i] = Integer.parseInt(st.nextToken());
        }

        dp[1] = 1;
        int res = 1;
        for (int i = 2; i <= N; i++) {
            dp[i] = 1;

            for (int j = 1; j < i; j++) {
                if(board[i]>board[j] && dp[i] <= dp[j]){
                    dp[i] = dp[j] + 1;
                }
            }
            res = Math.max(res , dp[i]);
        }

        System.out.println(res);
        br.close();
    }
}
