class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        // [1][1] 값을 tmp하나에 옮기기
        // 4번의 작업을 통해 옮겨야함.
        int[][]map = new int[rows+1][columns+1];
        int cnt = 1;
        for (int i=1;i<=rows;i++){
            for (int j=1;j<=columns;j++){
                map[i][j] = cnt++; 
            }
        }
        int i=0;
        for (int[]query :queries){
            int tmp = 0;
            int start_x = query[0];
            int start_y = query[1];
            int end_x = query[2];
            int end_y = query[3];
            //상
            tmp = map[start_x][end_y];
            int mn = tmp;
            for (int k=end_y;k>start_y;k--){
                map[start_x][k] = map[start_x][k-1];
                if (map[start_x][k]<mn)
                    mn = map[start_x][k];
            }
            //좌
            for (int k=start_x;k<end_x;k++){
                map[k][start_y] = map[k+1][start_y];
                if(map[k][start_y]<mn)
                    mn = map[k][start_y];
            }
            //하
            for (int k=start_y;k<end_y;k++){
                map[end_x][k]= map[end_x][k+1];
                if (map[end_x][k]<mn)
                    mn = map[end_x][k];
            }
            //우
            for (int k=end_x;k>start_x+1;k--){
                map[k][end_y] = map[k-1][end_y];
                if (map[k][end_y]<mn)
                    mn = map[k][end_y];
            }
            //tmp는 직접
            map[start_x+1][end_y] = tmp; 
            answer[i++] = mn;

        }
        
        return answer;
    }
}
