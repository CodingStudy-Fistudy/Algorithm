import java.io.*;

public class Main {
    static int[] num;
    static int[] oper;
    static int max = Integer.MIN_VALUE;
    static int min = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        num = new int[n];
        oper = new int[4];

        String[] inputNum = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            num[i] = Integer.parseInt(inputNum[i]);
        }

        String[] inputOper = br.readLine().split(" ");
        for (int i = 0; i < 4; i++) {
            oper[i] = Integer.parseInt(inputOper[i]);
        }

        calc(num[0], 1);
        
        System.out.println(max);
        System.out.println(min);
    }
  
    static int find(int a, int b, int op) {
        switch (op) {
            case 0: 
                return a + b;
            case 1: 
                return a - b;
            case 2: 
                return a * b;
            case 3: 
                return a < 0 ? -(-a / b) : a / b; //나누기 음수처리
            default:
                return 0;
        }
    }
    //재귀 반복
    static void calc(int result, int index) {
        if (index == num.length) {
            max = Math.max(max, result);
            min = Math.min(min, result);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (oper[i] > 0) {
                oper[i]--;
                int value = find(result, num[index], i);
                calc(value, index + 1);
                oper[i]++;
            }
        }
    }
}
