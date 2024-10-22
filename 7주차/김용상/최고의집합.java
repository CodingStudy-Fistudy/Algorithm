class Solution {
    public int[] solution(int n, int s) {
        int[] answer = new int[n];
        if (n>s) return new int[]{-1};
        
        int mok = s/n;
        for (int i=0;i<n;i++){
            answer[i] = mok;
        }
        for (int i=0;i<s%n;i++ ){
            answer[n-i-1]++; 
        }
        
        return answer;
    }
}
