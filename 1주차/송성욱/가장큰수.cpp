#include <string>
#include <vector>
#include <algorithm>
using namespace std;
//중요
bool cmp(string a, string b){

    return a+b>b+a;
}

string solution(vector<int> numbers) {
    vector<string> v;
    
    for(int i=0; i<numbers.size();i++)
    {
        v.push_back(to_string(numbers[i]));
    }
    string answer = "";
    
    //정렬
    sort(v.begin(),v.end(),cmp);
    
    
    if(v[0].compare("0")==0)
        return "0";
    
    for(int i=0; i<v.size();i++){
        answer+=v[i];
}
    return answer;
    
  
}
