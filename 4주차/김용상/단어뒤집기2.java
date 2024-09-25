import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        StringBuilder sb = new StringBuilder();
        Stack<Character> stack = new Stack<>();

        boolean InTag = false; 
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);

            if (ch == '<') { // '<' 일 때
                while (!stack.isEmpty()) { // 그 이전 스택에 쌓여있는 단어 뒤집어서 출력
                    sb.append(stack.pop());
                }
                InTag = true;
                sb.append(ch); // '<' 그대로 출력
            } else if (ch == '>') { // '>' 일 때
                InTag = false;
                sb.append(ch); // '>' 그대로 출력
            } else if (InTag) { // InTag 가 true 일 때 그대로 출력
                sb.append(ch);
            } else {
                if (ch != ' ') { // 공백이 아니면 스택에 넣기
                    stack.push(ch);
                } else { // 공백이면 한 단어를 스택에서 꺼내서 출력
                    while (!stack.isEmpty()) {
                        sb.append(stack.pop());
                    }
                    sb.append(' ');
                }
            }
        }

        // 마지막 단어가 남아있으면 뒤집어서 출력
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }

        System.out.println(sb);
    }
}
