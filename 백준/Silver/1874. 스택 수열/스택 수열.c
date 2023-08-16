#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TRUE 1

int top = -1;

void push(int* stack, int size, int cnt)
{
    if (top >= size - 1)
    {
        return;
    }
    else
    {
        stack[++top] = cnt;
    }
}

void pop(int* stack)
{
    if (top == -1)
    {
        return;
    }
    else stack[top--];
}

int main()
{
    int size;
    int n;
    int i;
    int cnt = 1;
    int op = 0;
    int flag = 0;

    int* stack;

    char* ans = "";

    scanf("%d", &size);

    ans = (char*)malloc( sizeof(char) * size * 2);
    stack = (int*)malloc(sizeof(int) * size);

    getchar();
    for (i = 0; i < size; i++)
    {
        scanf("%d", &n);

        while (TRUE)
        {
            if (stack[top] < n)
            {
                push(stack, size, cnt);
                cnt++;
                ans[op++] = '+';
            }
            else if ( stack[top] == n)
            {
                pop(stack);
                ans[op++] = '-';
                break;
            }
            else
            {
                flag = 1;
                break;
            }
            
        }

        if (flag == 1)
        {
            printf("NO");
            return 0;
        }
       
    }

    for (i = 0; i < op; i++)
    {
        printf("%c\n", ans[i]);
    }

    free(stack);
    free(ans);

    return 0;
}


/*

8
4
3
6
8
7
5
2
1

5
1
2
5
3
4

*/