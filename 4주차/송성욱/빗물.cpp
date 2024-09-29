#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T;
    int n, m, k;
    int X, Y;
    int answer = 0;

    cin >> n >> m;
    vector<int> v(m);

    for (int i = 0; i < m; i++)
        cin >> v[i];

    for (int i = 1; i < m - 1; i++) {
        int left = 0; int right = 0;
      
        for (int j = 0; j < i; j++) 
        {
            left = max(left, v[j]);
        }
        for (int j = m - 1; j > i; j--) 
        {
            right = max(right, v[j]);
        }
        
        answer += max(0, min(left, right) - v[i]);
    }

    cout << answer << endl;
    return 0;
}
