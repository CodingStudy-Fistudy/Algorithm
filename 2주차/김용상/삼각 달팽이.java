import java.util.*;
class Solution {
    public int[] solution(int n) {
        //패턴 존재
        int[] answer = {};
        int[][]list = new int[n+1][n+1];
       
        // n==4 -> 4,3,2,1 = 10 
        // n--5 -> 5,4,3,2,1 = 15 
        // n==6 -> 6,5,4,3,2,1 = 21 
        int a = n;
        int cnt = 0;
        int x = -1;
        int y = 0;
        int num = 0;
        
        while(a>=1){
            //세로 진행
            if (cnt%3==0){
                //아래로
                x+=1;
                for (int i=x;i<x+a;i++){
                    list[i][y] = ++num;
                }
                x = x+a-1;
                y+=1;
            }
             else if (cnt%3==2){   
                //위로
                for (int i=x;i>x-a;i--){
                     y-=1;
                    
                    list[i][y] = ++num;
                    
                }
                 
                x = x-a+1;
            }           
            //가로 진행
            else if (cnt%3==1) {
                //오른쪽으로
               for (int i=y;i<y+a;i++){
                   list[x][i] = ++num;
                }
                y = y+a-1;
                x-=1;               
            }                
            a--;
            cnt+=1;
        }
      
        int[]lst = new int[num];
        int k = 0;
        for (int i=0;i<list.length;i++){
            for (int j=0;j<list.length;j++){
                if (list[i][j]==0) continue;
                lst[k++] = list[i][j];
            }
        }
        return lst;
    }
}
