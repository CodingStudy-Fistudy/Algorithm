#include <string>
#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
int answer=0;


void dfs(vector<int>numbers, int target, int i, int num)
{
    
    if(num==target&&i==numbers.size())
    {
        answer++;
        return;
    }
    //재귀구현 생각을 못했다..... DFS...
    if(i<numbers.size())
    {
        dfs(numbers,target,i+1,num+numbers[i]);
        
        dfs(numbers,target,i+1,num-numbers[i]);
    }
    
}

int solution(vector<int> numbers, int target) {
    
 
    
    dfs(numbers, target, 0 ,0);
    
    return answer;
}
