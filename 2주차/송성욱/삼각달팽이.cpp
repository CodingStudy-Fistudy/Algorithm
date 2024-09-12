#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) 
{
	vector<int> answer;
	vector<vector<int>> snail(n, vector<int>(n));
	int value = 1, way = 0, y = 0, x = 0;
     //n만큼 방향을 바꾼다
	for ( int i = 0; i < n; i++)
	{
		switch (way)
		{
		// 아래
		case 0:
			for (int j = i; j < n; j++)
			{
				snail[y++][x] = value++;
			}
			y--;
			x++;
			way = 1;
			break;
		// 옆
		case 1:
			for (int j = i; j < n; j++)
			{
				snail[y][x++] = value++;
			}
			y--;
			x -= 2;
			way = 2;
			break;
                
		// 대각선
		case 2:
			for (int j = i; j < n; j++)
			{
				snail[y--][x--] = value++;
			}
			y += 2;
			x++;
			way = 0;
			break;
		}
	}

	// input answer
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < i + 1; j++)
		{
			answer.push_back(snail[i][j]);
		}
	}

	return answer;
}
