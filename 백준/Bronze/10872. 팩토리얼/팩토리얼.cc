#include<iostream>

using namespace std;

int fac(int n)
{
    if (n <= 1) return 1;
    return fac(n - 1) * n;
}

int main()
{
    int n;
    cin >> n;

    int tmp = fac(n);

    cout << tmp << endl;

}