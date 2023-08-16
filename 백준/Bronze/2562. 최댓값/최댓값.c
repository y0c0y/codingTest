#pragma warning(disable:4996)
#include <stdio.h>
int main()
{
    int max, i, a = 1, list[9];

    for (int i = 0; i < 9; i++)
    {
        scanf("%d", &list[i]);
    }

    max = list[0];

    for (int i = 0; i < 9; i++)
    {
        if (list[i] > max)
        {
            max = list[i];
            a = i + 1;
        }
    }
    printf("%d\n%d", max, a);
}