import java.util.*;
class Solution {
    public int[] solution(String[] maps) {
        int[] answer = {};
        int []dx = new int[]{-1,1,0,0};
        int []dy = new int[]{0,0,-1,1};
        int n = maps.length;
        int m = maps[0].length();
        int[][]mp = new int[n][m];
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                mp[i][j] = (int)maps[i].charAt(j)-'0';
            }
        }
        List<Integer>lst = new ArrayList<>();
        boolean[][]visited = new boolean[n][m];
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){                
                if(visited[i][j]||mp[i][j]>=10)
                    continue;
                int cnt = 0;
                Deque<Node>dq = new ArrayDeque<>();
                dq.add(new Node(i,j,mp[i][j]));
                while(!dq.isEmpty()){
                    Node poll = dq.poll();
                    if (visited[poll.x][poll.y])
                        continue;
                    visited[poll.x][poll.y] = true; 
                    cnt+=poll.sm;
                    for(int k=0;k<4;k++){
                        int nx = dx[k]+poll.x;
                        int ny = dy[k]+poll.y;
                        if (nx>=0&&nx<n&&ny>=0&&ny<m&&!visited[nx][ny]&&mp[nx][ny]<10){
                            dq.add(new Node(nx,ny,mp[nx][ny]));
                        }
                    }            
                }
                if (cnt!=0)
                    lst.add(cnt);

            }
        }
        if (lst.size()==0) return new int[]{-1};
        Collections.sort(lst);                   
        answer = new int[lst.size()];
        for (int i=0;i<lst.size();i++){
            answer[i] = lst.get(i);
        }
        return answer;
    }
}
class Node{
    int x;
    int y;
    int sm;
    public Node(int x,int y,int sm){
        this.x = x;
        this.y = y;
        this.sm = sm;
    }
}
