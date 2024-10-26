#include<iostream>
#include<vector>
#include<algorithm>
#include<limits.h>

using namespace std;

int n, m;
vector<bool> visited;
vector<vector<int>> comb;

void DFS(int s, int cnt) {
	if (cnt == m) {
		vector<int> c;
		for (int i = 0; i < visited.size(); i++) {
			if (visited[i] == true) {
				c.push_back(i);
			}
		}
		comb.push_back(c);
		return;
	}

	for (int i = s; i < visited.size(); i++) {
		if (visited[i]) continue;
		visited[i] = true;
		DFS(i, cnt + 1);
		visited[i] = false;
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;

	int temp;
	vector<pair<int, int>> chichen;
	vector<pair<int, int>> home;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> temp;
			if (temp == 1) {
				home.push_back(pair<int, int>(i, j));
			}
			else if (temp == 2) {
				chichen.push_back(pair<int, int>(i, j));
			}
		}
	}

	visited.resize(chichen.size());

	DFS(0, 0);

	int answer = INT_MAX;
	for (int i = 0; i < comb.size(); i++) {
		int dis = 0;
		for (int j = 0; j < home.size(); j++) {
			int m = INT_MAX;
			for (int k = 0; k < comb[i].size(); k++) {
				int index = comb[i][k];
				m = min(m, abs(home[j].first - chichen[index].first) + abs(home[j].second - chichen[index].second));//내 집에서 이 치킨집까지 거리
			}
			dis += m;
		}
		answer = min(answer, dis);
	}

	cout << answer;
	return 0;

}
