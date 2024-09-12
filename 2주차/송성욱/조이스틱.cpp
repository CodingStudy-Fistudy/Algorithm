#include <string>
#include <vector>
#include <algorithm>
 
using namespace std;
 
int solution(string name) {
    int answer = 0; 
    
    //A변경 순방향 이동 역방향 이동 
    for(auto ch: name) answer += min(ch - 'A', 91 - ch);
 
    int len = name.length();
    int move = len - 1;
    int next;
    
    for(int i = 0; i < len; i++) {
        next = i + 1;
        //a연속시 처리
        while(next < len && name[next] == 'A') next++;
        
        move = min(move, i + (len - next) + min(i, len - next));
    }
    answer += move;
 
    return answer;
}
