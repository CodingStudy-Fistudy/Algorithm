// 단어수가 20개 이하라서, dfs로 풀 수 있겠다고 생각

class Solution {
    private int cnt=0;
    private int[] oper = {1,-1};
    private int target, length;
    public int solution(int[] numbers, int target) {
        this.target=target;
        this.length=numbers.length;
        dfs(numbers, 0, 0);

        return cnt;
    }
    
    public void dfs(int[] numbers,int sum, int depth){
        if(length==depth){
            if(sum==target){
                cnt++;
            }
            return;
        }
        for(int i=0; i<2; i++){
            sum+=numbers[depth]*oper[i];
            dfs(numbers,sum,depth+1);
            sum-=numbers[depth]*oper[i];
        }
    }
}
