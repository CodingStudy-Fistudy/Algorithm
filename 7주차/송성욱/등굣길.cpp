#include <string>
#include <vector>

using namespace std;

int solution(int m, int n, vector<vector<int>> puddles) 
{
    int answer = 0;
    int road[100][100];
    
   
    for(int i = 0; i < 100; ++i){
        for(int j = 0; j < 100; ++j)
            road[i][j] = -1;
    }
    
    road[0][0] = 1;
    
   
    for(int i = 0; i < puddles.size(); ++i)
        road[puddles[i][0]-1][puddles[i][1]-1] = 0;
    
    
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; ++j)
        {
            if(road[i][j] == -1)
            {
                if(i == 0 && j == 0)
                    continue;
                else if(i == 0)
                    road[i][j] = road[i][j-1] % 1000000007;
                else if(j == 0)
                    road[i][j] = road[i-1][j] % 1000000007;
                else
                    road[i][j] = (road[i][j-1] + road[i-1][j]) % 1000000007;
            }
        }
    }
    
    answer = road[m-1][n-1];
    return answer;
}

