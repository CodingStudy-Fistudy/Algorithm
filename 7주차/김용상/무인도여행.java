import java.util.*;
class Solution {
    public int[] solution(String[] maps) {
        int n = maps.length;
        int m = maps[0].length();
        int[]dx = new int[]{-1,1,0,0};
        int[]dy = new int[]{0,0,-1,1};
        boolean[][]visited = new boolean[n][m];
        List<Integer>list = new ArrayList<>();
        Deque<Node>dq = new ArrayDeque<>();
        
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                if (!visited[i][j]&&maps[i].charAt(j)!='X'){
                   System.out.println(maps[i].charAt(j)-'0');
                    
                    int c = 0;
                    dq.add(new Node(i,j));
                    while(true){
                        if (dq.isEmpty()){
                            list.add(c);
                            break;
                        }
                        Node poll = dq.poll();
                        if (visited[poll.x][poll.y]){
                            continue;
                        }
                        visited[poll.x][poll.y] = true;
                        c+=maps[poll.x].charAt(poll.y)-'0';
                       
                        for (int k=0;k<4;k++){
                            int nx = poll.x+dx[k];
                            int ny = poll.y+dy[k];
                            if (nx>=0&&nx<n&&ny>=0&&ny<m&&!visited[nx][ny]&&maps[nx].charAt(ny)!='X'){
                                dq.add(new Node(nx,ny));
                            }
                        }
                        
                    }
                }
            }
        }
        if (list.size()==0) 
            return new int[]{-1};
            
        int[] answer = new int[list.size()];
        
        
        Collections.sort(list);
        for (int i=0;i<list.size();i++){
            answer[i] = list.get(i);
        }
        
        return answer;
    }
    
}
class Node{
    int x;
    int y;
    public Node(int x,int y){
        this.x = x;
        this.y = y;
    }
}
