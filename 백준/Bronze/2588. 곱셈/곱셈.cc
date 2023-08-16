#include<iostream>
#include<string>

using namespace std;


int main(void)
{
	int n1, n2;
	int first, second, thrid;

	cin >> n1 >> n2;



	thrid = n2 % 10;
	thrid *= n1;

	cout << thrid << "\n";


	

	second = n2 / 10 % 10;
	second *= n1;

	cout << second << "\n";

	second *= 10;

	first = n2 / 100;

	first *= n1;

	cout << first << "\n";
	
	first *= 100;


	cout << (first + second + thrid) << "\n";

	return 0;
}