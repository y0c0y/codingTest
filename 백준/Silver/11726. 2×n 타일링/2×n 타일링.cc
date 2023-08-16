#include <iostream>
#include <vector>
using namespace std;

vector<int> dp;

int tile(int n) {
    if (n == 1 || n == 2) return n;
    // 이미 값을 계산한 적이 있다면 그 값을 바로 리턴
    if (dp[n] != -1) return dp[n];
    // 아니라면 계산해서 dp 리스트에 넣어 보존
    dp[n] = (tile(n - 2) + tile(n - 1)) % 10007;
    return dp[n] ;
}

int main() {
    int N;
    cin >> N;
    dp.resize(N + 1, -1); // 초기값 -1은 fibonacci 결과로 절대 나올 수 없는 값
    cout << tile(N);
}

