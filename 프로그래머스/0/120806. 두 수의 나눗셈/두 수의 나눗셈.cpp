#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int num1, int num2) {
    int answer = 0;
    float tmp = num1*1.0/num2*1.0;

    answer = tmp*1000;

    return answer;
}