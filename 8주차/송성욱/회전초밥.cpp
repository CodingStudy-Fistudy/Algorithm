#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int n, d, k, c; 
int arr[30001]; 
bool check[30001];
int maxCnt = 0;

int main() 
{
    cin >> n >> d >> k >> c;
    for(int i = 0; i < n; i++) 
    {
        cin >> arr[i];
    }

    for(int i = 0; i < n; i++) 
    {
        int flag = 0;
        int coupon = 1;
        for(int j = i; j < i + k; j++) 
        {
            if(!check[arr[j % n]]) 
                check[arr[j % n]] = true;
            else flag++;
        }
        if(check[c]) coupon = 0;
        maxCnt = max(maxCnt, k - flag + coupon);
        memset(check, false, sizeof(check));
    }
    cout << maxCnt << endl;
    return 0;
}
