#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
vector<string> answer;
bool visited[100000001];
bool check = false;


void DFS(string airport,vector<vector<string>> tickets,int count)
{
    if(count==tickets.size())
        check=true;
    answer.push_back(airport);
    for(int i=0;i<tickets.size();i++)
    {
        if(!visited[i]&&tickets[i][0]==airport)
        {
            visited[i]=true;
            DFS(tickets[i][1],tickets,count+1);
            
            if(!check)
            {
                answer.pop_back();
                visited[i]=false;
            }
        }
            
    }
    
}

vector<string> solution(vector<vector<string>> tickets)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    sort(tickets.begin(), tickets.end());
    
    DFS("ICN",tickets,0);
    
    return answer;
}
