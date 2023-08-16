#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<pair<int, string>> arr;

bool comp(const pair<int, string>& a, const pair<int, string>& b)
{
	return a.first < b.first;
}

int main()
{
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

	int n;

	cin >> n;

	for (int i = 0; i < n; ++i)
	{
		int t;
		string ts;
		cin >> t >> ts;
		arr.push_back({ t, ts });
	}

	stable_sort(arr.begin(), arr.end(), comp);

	for (auto& data : arr)
	{
		cout << data.first << ' ' << data.second << '\n';
	}

	return 0;
}