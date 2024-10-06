#include <iostream>
 
using namespace std;
typedef long long LL;
 
LL dp[110][110];
int map[110][110];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N; 
    cin >> N;
    for(int j=0; j<N; j++) 
    {
        for(int i=0; i<N; i++)
        {
            cin >> map[j][i];
        }
    }
    
    fill(&dp[0][0], &dp[109][110], 0);
    dp[0][0] = 1;
    for(int j=0; j<N; j++) 
    {
        for(int i=0; i<N; i++) 
        {
            int k = map[j][i];
            if(k==0) continue;
            dp[j+k][i] += dp[j][i];
            dp[j][i+k] += dp[j][i];
        }
    }
    
    cout << dp[N-1][N-1]<< '\n';
    
    return 0;
}
