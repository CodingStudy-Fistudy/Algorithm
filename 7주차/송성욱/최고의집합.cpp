#include <string>
#include <vector>
#include <iostream>


using namespace std;

vector<int> solution(int n, int s) 
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    vector<int> answer;
    if(n > s){
        answer.emplace_back(-1);
        return answer;
    }
    int quo = s / n;
    int rem = s % n;
    int num = 0;
    
    if(s % n != 0) 
    {
        num = 1; 
    }
    for(int i = 0; i < n; i++)
    {
        if(i >= n - rem) 
        {
            answer.emplace_back(quo + 1);
        }
         else 
         {
             answer.emplace_back(quo);
    
         }
    }
    return answer;
}
