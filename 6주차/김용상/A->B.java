import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        long a= Integer.parseInt(s[0]);
        long b =Integer.parseInt(s[1]);

        Deque<Node1>dq = new ArrayDeque<>();

        dq.add(new Node1(a,1));
        long cnt = 1;
        while(!dq.isEmpty()){
            Node1 poll = dq.poll();
            if (poll.num==b) {
                cnt = poll.dep;
                break;
            }
            else if (poll.num>b) {
                continue;
            }
            dq.add(new Node1(poll.num*2,poll.dep+1));

            dq.add(new Node1(poll.num*10+1, poll.dep+1));

        }
        System.out.println(cnt==1?-1:cnt);

    }
    public static class Node1{
        long num;
        long dep;
        public Node1(long num,long dep){
            this.num = num;
            this.dep = dep;
        }
    }

}
