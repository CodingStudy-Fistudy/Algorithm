import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        int n = numbers.length;
        int[] answer = new int[n];
        Arrays.fill(answer,-1);
        // n log n으로 끝내야함
        Stack<Node>st = new Stack<Node>();
        for (int i=0;i<n;i++){
            while(!st.isEmpty()){
                Node peek = st.peek();
                if (numbers[i]>peek.num){
                    st.pop();
                    answer[peek.idx] = numbers[i];
                    continue;
                }
                break;
            }                  
            st.push(new Node(numbers[i],i));
        }
        return answer;
    }
}
class Node{
    int num;
    int idx;
    public Node(int n,int x){
        this.num = n;
        this.idx = x;
    }
} 
