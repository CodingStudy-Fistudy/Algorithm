#include <string>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int carpet = yellow + brown;

    //sqrt 제곱근 반환 함수사용 생각못함

    for (int height = 3; height <= sqrt(carpet); height++)
    {
        if (carpet % height == 0)
        {
            int width = carpet / height;


            if (((width + height) * 2 - 4) == brown)
            {
                answer.push_back(width);
                answer.push_back(height);
                break;
            }

        }


    }


    return answer;
}
//예제 입력
//int main() 
//{
//   
//
//   
//    int brown = 10;
//    int yellow = 2;
//
//   
//    vector<int> result = solution(brown, yellow);
//
//    cout << "Width: " << result[0] << ", Height: " << result[1] << endl;
//
//    return 0;
//}
