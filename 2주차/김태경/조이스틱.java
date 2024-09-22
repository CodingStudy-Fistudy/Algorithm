class Solution {
    int answer = 0;
    
    public int solution(String name) {
        run(name.toCharArray()); 
        return answer;
    }
    
    void run(char[] name) {
        int length = name.length;
        char[] now = new char[length];
        
        for (int i = 0; i < length; i++) {
            now[i] = 'A';
        }
        
        int move = length - 1;  
        
        for(int idx=0;idx<length;idx++){
            if (now[idx] != name[idx]) {
                int up = name[idx] - 'A';  
                int down = 'Z' - name[idx] + 1;  
                answer += Math.min(up, down); 
                now[idx] = name[idx];  
            }
            

            
            int index = idx + 1;  
            while (index < length && name[index] == 'A') {
                index++;
            }
            move = Math.min(move, idx * 2 + length - index);
            move = Math.min(move, (length - index) * 2 + idx);
            
        }
        
        answer += move;
    }
}
