#include<iostream>
#include <string>
#include <math.h>
using namespace std;

int main()
{
    int n;
    int cnt = 0;
    cin >> n;

    int len = to_string(n).length();

   
    for (int i = 0; i < len; i++)
    {
        cnt += n - ((int)pow(10, i) - 1);
    }

    cout << cnt << endl;


}