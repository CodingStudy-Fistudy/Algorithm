import java.util.*;
class Solution {
    int[] dx={1,0,-1,0};
    int[] dy={0,1,0,-1};
    boolean[][] visited;
    int x,y;
    int[][] dp;
    public int solution(String[] board) {
        int answer = 0;
        x=board.length;
        y=board[0].length();
        visited=new boolean[x][y];
        dp=new int[x][y];
        
        for(int i=0;i<x;i++){
            for(int j=0;j<y;j++){
                if(board[i].charAt(j)=='R'){
                    answer=bfs(i,j,board);
                    break;
                }
            }
            
        }
        
        return answer;
    }
    int bfs(int xidx, int yidx, String[] board){
        //System.out.println(xidx+" "+ yidx);
        visited[xidx][yidx]=true;
        ArrayDeque<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[]{xidx,yidx});
        while(!dq.isEmpty()){
            int[] now = dq.poll();
            for(int i=0;i<4;i++){
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];
                if(nx<0 || nx>=x || ny<0 || ny>=y || board[nx].charAt(ny)=='D'){
                    continue;
                }
                int flag=0;
                while(nx>=0 && nx<x && ny>=0 && ny<y && board[nx].charAt(ny)!='D'){
                    nx+=dx[i];
                    ny+=dy[i];
                    flag=1;
                }
                if(flag==1){
                    nx-=dx[i];
                    ny-=dy[i];
                }
                if(visited[nx][ny]){
                    continue;
                }
                
                
                if(board[nx].charAt(ny)=='G'){
                    return dp[now[0]][now[1]]+1;
                }
                visited[nx][ny]=true;
                dp[nx][ny]=dp[now[0]][now[1]]+1;
                dq.offer(new int[]{nx,ny});
                
            }
        }
        return -1;
    }
}
