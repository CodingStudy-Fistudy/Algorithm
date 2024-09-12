#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>


using namespace std;



long long solution(string expression) {
    long long answer = 0;
    vector <long long> num;  //숫자 벡터
    vector <char> exp, location; //연산자의 종류 , 위치 
    string n=""; //문자열 형태의 숫자를 저장하는 n
    
    for(int i=0;i<expression.size();i++)
    {
        if(expression[i]=='+'||expression[i]=='-'||expression[i]=='*')
        {
            num.push_back(stoi(n)); //초기화!! 초기화 구현 생각못함!!
            n="";
            if(find(exp.begin(),exp.end(),expression[i])==exp.end())
                exp.push_back(expression[i]);
            location.push_back(expression[i]); 
            
        }
        else
            n+=expression[i];
        
        
    }
    num.push_back(stoi(n));
    sort(exp.begin(),exp.end()); //연산자 순렬을 구하기 위해 정렬하기
    
    
    do
    {
        vector<long long> tmp_num=num; //임시저장 백터들
        vector<char> tmp_loc=location;
        
        for(int i=0;i<exp.size();i++)
        {
            for(int j=0;j<tmp_loc.size();j++)
            {
                if(exp[i]==tmp_loc[j])
                {
                    if(tmp_loc[j]=='+')
                        tmp_num[j]=tmp_num[j]+tmp_num[j+1];
                    else if(tmp_loc[j]=='-')
                        tmp_num[j]=tmp_num[j]-tmp_num[j+1];
                    else if(tmp_loc[j]=='*')
                        tmp_num[j]=tmp_num[j]*tmp_num[j+1];
                    
                    tmp_num.erase(tmp_num.begin()+j+1); 
                    tmp_loc.erase(tmp_loc.begin()+j);
                    j--;
                }
            }
            
        }
        
        if(answer<abs(tmp_num[0]))
            answer=abs(tmp_num[0]);
    }while(next_permutation(exp.begin(),exp.end())); //순열만들기
    
    
        
    
   return answer;
}
