#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int solution(int n, vector<vector<int>> edge) 
{
    int answer = 0;
    int from, to; 
    vector <vector<int>> graph(n+1); 
    vector <int> dist(n+1, -1); 
    for(int i=0; i<edge.size(); i++)
    {
        from = edge[i][0]; 
        to = edge[i][1]; 
        graph[from].push_back(to);     
        graph[to].push_back(from); 
    }
    queue<int> q; 
    q.push(1); 
    dist[1]=0; 
    while(!q.empty()){
        int current = q.front(); 
        q.pop(); 
        int d = dist[current]; 
        for(int i=0; i<graph[current].size(); i++){
            int next = graph[current][i]; 
            if(dist[next]!=-1)continue; 
            dist[next] = d+1;      
            q.push(next); 
        }
    }
    sort(dist.begin(), dist.end(), greater<int>()); 
    int pos = 0; 
    while(dist[pos++]==dist[0]){
        answer++; 
    }
    return answer;
}
