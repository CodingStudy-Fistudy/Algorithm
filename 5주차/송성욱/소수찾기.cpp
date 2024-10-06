#include <string>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

map<int, bool> M;

bool isPrime(string num){
    int n = stoi(num);
    
    if(M[n]) 
        {return false;}
    
    M[n] = true;
    if(n == 1 || n == 0) 
    {
        return false;
    }
    
    if(n == 2) 
    {
        return true;
    }
    for(int i=2; i<=sqrt(n); i++)
    {
        if(n % i == 0)
        { 
            M[n] == -1;
            return false;
        }              
    }
    M[n] == 1;
    return true;
}

int solution(string numbers) 
{
    
    int answer = 0;
    
    sort(numbers.begin(), numbers.end());
    
    do{
        for(int i=1; i<=numbers.size(); i++){
            string num = numbers.substr(0, i);         
            if(isPrime(num)) answer++;
        }
    }while(next_permutation(numbers.begin(), numbers.end()));
    
    return answer;
}
