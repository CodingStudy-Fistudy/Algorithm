#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <cmath>
#include <string.h>


using namespace std;

int dx[4]={-1,0,1,0};
int dy[4]={0,1,0,-1}; //북동남서


int solution(vector<string> board) 
{
    
    int n=board.size();
    int m=board[0].size();
    
    int visited[100][100];
    memset(visited,-1,sizeof(visited));// 방문배열 -1로 초기화
    queue<pair<int,int>> q;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(board[i][j]=='R')
                q.push({i,j});
            
        }    
    }
        visited[q.front().first][q.front().second]=0; //시작점 이동횟수
            while(!q.empty())
            {
                
                pair<int,int> cur=q.front();
                q.pop();
                for(int dir=0;dir<4;dir++)
                {
                    int nx=cur.first;
                    int ny=cur.second;
                    
                    while(1)
                    {
                        if(nx<0||ny<0||nx>=n||ny>=m)
                            break;
                        if(board[nx][ny]=='D')
                            break;
                        
                        //전진하는거
                        nx+=dx[dir];
                        ny+=dy[dir];
                    }
                    
                    nx-=dx[dir]; //벽 또는 장애물일때까지 전진했기 때문에
                    ny-=dy[dir];// 이전 좌표에서 멈춰야한다
                    if(board[nx][ny]=='G')
                        return (visited[cur.first][cur.second]+1);
                    
                    if(visited[nx][ny]>=0)
                        continue;
                    visited[nx][ny]=visited[cur.first][cur.second]+1;
                    
                    q.push({nx,ny});
                    
                }
                
            }
            return (-1);
        
    
    
    
    
    
}
