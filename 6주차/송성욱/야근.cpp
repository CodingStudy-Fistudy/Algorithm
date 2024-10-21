#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

long long solution(int n, vector<int> works) {    
    long long answer = 0;
    priority_queue<int>que;
    int num,cnt;
    
    for(int i=0; i<works.size(); i++)
        que.push(works[i]);
    
    for(int i=0; i<n; i++){
        num=que.top();
        que.pop();
        if(num-1>0)
            que.push(num-1);
        
        if(que.empty()==1)
            return 0;
    }
    
    while(que.empty()!=1){
        answer+=que.top()*que.top();
        que.pop();
    }
        
    return answer;
}
