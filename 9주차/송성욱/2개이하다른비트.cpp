#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<long long> solution(vector<long long> numbers)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    vector<long long> answer;
    for(int i = 0; i < numbers.size();i++){
        if(numbers[i] % 2 == 0)
            answer.push_back(numbers[i] + 1);
        //홀수인 경우 생각하기 어려웠음
        else
        {
            long long bit = 1;
            while(1){
                if((numbers[i] & bit) == 0)
                    break;
                bit *= 2;
            }
            bit /= 2;
            answer.push_back(numbers[i] + bit);
        }
    }
    return answer;
}
