import java.util.*;

class Solution {
    boolean visited[][];
    int[][] map;
    int[] dx={1,0,-1};
    int[] dy={0,1,-1};
    public int[] solution(int n) {
        visited=new boolean[n][n];
        map=new int[n][n];
        
        
        run(n);
        ArrayList<Integer> ans = new ArrayList<>();
        for(int i=0;i<n;i++){
            for(int j=0;j<i+1;j++){
                ans.add(map[i][j]);
            }
        }
        int answer[] = ans.stream()
                        .mapToInt(Integer::intValue)
                        .toArray();
        return answer;
    }
    void run(int n){
        int i=0, j=0, dir=0, num=1;
        visited[i][j]=true;
        map[i][j]=num;
        while(true){
            int nx=i+dx[dir];
            int ny=j+dy[dir];
            if(nx>=n || nx<0 || ny>=n || ny<0 || visited[nx][ny]){
                dir=(dir+1)%3;
                nx=i+dx[dir];
                ny=j+dy[dir];
            }
            //전환했는데도 이동 못하면 종료
            if(nx>=n || nx<0 || ny>=n || ny<0 || visited[nx][ny]){
                break;
            }
            
            i=nx;
            j=ny;
            num++;
            map[i][j]=num;
            visited[i][j]=true;
            
            
        
            
        }
    }
}
