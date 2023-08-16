#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#define STACK_SIZE 10000

/*
push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
*/

typedef int element;
element stack[STACK_SIZE];
int top = -1;

void push(element item)
{
	if (top >= STACK_SIZE - 1)
	{
		printf("\n\n Stack is FULL ! \n");
		return;
	}
	else stack[++top] = item;
}

element pop()
{
	if (top == -1)
	{
		//printf("\n\n Stack is Empty ! \n");
		return -1;
	}
	else return stack[top--];
}

element peek()
{
	if (top == -1)
	{
		//printf("\n\n Stack is Empty ! \n");
		return -1;
	}
	else return stack[top];
}

/*void printStack()
{
	int i;
	printf("\n Stack [ ");

	for (i = 0; i <= top; i++)
	{
		printf("%d", stack[i]);
	}
	printf("] ");
}*/

int main()
{
	int n;
	int item;
	int i;

	char comment[6] = "";

	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{
		scanf("%s", comment);

		if (strcmp(comment, "push") == 0)
		{
			scanf("%d", &item);
			push(item);
		}

		if (strcmp(comment, "top") == 0)
		{
			item = peek();
			printf("%d\n", item);
		}
		if (strcmp(comment, "size") == 0)
		{
			printf("%d\n", top + 1);

		}
		if (strcmp(comment, "empty") == 0)
		{
			if(top + 1 > 0) printf("0\n");
			else printf("1\n");

		}
		if (strcmp(comment, "pop") == 0)
		{
			item = pop();
			printf("%d\n", item);
		}

	}

	return 0;
}

/*
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
*/