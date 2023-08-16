#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;

string s;
set<string> list;

void combination(int start, int len)
{

	list.insert(s.substr(start, len));
	
	if (start == s.length()) return;

	if (len == s.length() - start) combination(start + 1, 1);
	else combination(start, len + 1);	

}

int main(void)
{

	cin >> s;

	int start = 0;
	int len = 1;

	combination(start, len);

	cout << list.size()-1;
	
	return 0;
}


/*

15
*/