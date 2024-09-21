import java.util.*;

class Solution {
    ArrayList<Long> value = new ArrayList<>();
    ArrayList<Character> operater = new ArrayList<>();
    char[] op = new char[]{'-','+','*'};
    boolean[] visited =new boolean[3];
    ArrayList<Character> seq=new ArrayList<>();
    long answer = 0;
    public long solution(String expression) {
        //long answer = 0;
        div(expression,expression.length());
        
        perm(0);
        return answer;
    }
    void div(String ex, int len){
        int idx=0;
        for(int i=0;i<len;i++){
            if(ex.charAt(i)=='-' || ex.charAt(i)=='*' || ex.charAt(i)=='+'){
                operater.add(ex.charAt(i));
                System.out.println(ex.substring(idx,i));
                value.add(Long.parseLong(ex.substring(idx,i)));
                idx=i+1;
            }
        }
        value.add(Long.parseLong(ex.substring(idx)));
        //System.out.println(value);
    }
    void perm(int depth){
        
        if(depth==3){
            //System.out.println(seq);
            answer=Math.max(answer,Math.abs(oper()));
        }
        for(int i=0;i<3;i++){
            if(!visited[i]){
                visited[i]=true;
                seq.add(op[i]);
                perm(depth+1);
                seq.remove(seq.size()-1);
                visited[i]=false;
            }
            
        }
        
    }
    
    long oper(){
        ArrayList<Long> tvalue = new ArrayList<>(value);
        ArrayList<Character> toperater = new ArrayList<>(operater);
        
        
        for(char o : seq){
            int idx=0;
            while(toperater.size()>idx){
                if(o==toperater.get(idx)){
                    tvalue.add(idx,cal(tvalue.remove(idx), tvalue.remove(idx), toperater.remove(idx)));
                }else{
                    idx++;
                }
            }
        }
        return tvalue.get(0);
    }
    long cal(long left, long right, char o){
        switch(o){
                case '-'-> {return left-right;}
                case '+'-> {return left+right;}
                case '*'-> {return left*right;}
                default ->{return 0;}
        }
    }
}
