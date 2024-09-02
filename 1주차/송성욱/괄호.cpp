#include <iostream>
#include <string>
#include <stack>

using namespace std;

bool solution(string s)
{
    stack<char> stk;
    for (char& c : s) {
        if (c == '(')
            stk.push(c);
        else {
            if (stk.empty())
                return false;
            else
                stk.pop();
        }
    }
    return stk.empty();
}
//돌리는거
//int main()
//{
//
//
//    string s = "(()())";
//
//   
//    if (solution(s))
//        cout << "올바른 괄호입니다." << endl;
//    else
//        cout << "올바르지 않은 괄호입니다." << endl;
//
//    return 0;
//
//
//
//}
