#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer={0,0};
    vector<pair<int,int>> number;
    
    priority_queue<pair<int,int>> maxQ; //최대값 삭제
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> minQ; //최소값 삭제
    
    int deleteCnt=0;
    
    for(auto& a:operations){
        int num=stoi(a.substr(2,a.size()));

        if(a[0]=='I')
        {
            number.push_back(make_pair(num,0)); //두 객체를 하나로 묶어주는것
            maxQ.push(make_pair(num,number.size()-1));
            minQ.push(make_pair(num,number.size()-1));
        }
        else {
            if(a[2]=='1')
            {
                if(deleteCnt==number.size())
                    continue;
                
                int deleteIdx=maxQ.top().second;
                number[deleteIdx].second=1;
                maxQ.pop();
                deleteCnt++;
            }
            else
            {
              if(deleteCnt==number.size())
                  continue;
                int deleteIdx=minQ.top().second;
                number[deleteIdx].second=1;
                minQ.pop();
                deleteCnt++;
            }
           
        }
        
    }
    if(deleteCnt==number.size())// 큐가 비었다면 [0,0] 리턴
    { 
        return answer;
    }
    vector<int> tmp;
   
    for(auto& num:number)
    {
        if(num.second==0) // 삭제되지 않은 숫자만 따로 추출
        { 
            tmp.push_back(num.first);
        }
    }
    int maxVal= *max_element(tmp.begin(),tmp.end());
    int minVal= *min_element(tmp.begin(),tmp.end());
    answer[0]=maxVal;
    answer[1]=minVal;

    return answer;
}d
