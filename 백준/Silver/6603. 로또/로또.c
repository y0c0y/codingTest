#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void DFS(int *S, int * Flag, int size, int index, int cnt)
{
	int i = 0;
	
	if (size - index < 6 - cnt)
		return;

	if (cnt == 6)
	{
		for (i = 0; i < size; i++)
			if (Flag[i] == 1)
				printf("%d ", S[i]);
	
		printf("\n");

		return;
	}
    
	else
	{
		Flag[index] = 1;
		DFS(S, Flag, size, index + 1, cnt + 1);
		Flag[index] = 0;
		DFS(S, Flag, size, index + 1, cnt);
	}
}

int main()
{
	int * S, * Flag;
	int n, i;
	int cnt = 0;

	while (1)
	{
		scanf("%d", &n);

		if (n == 0)
		    break;
		
		cnt = 0;

		S = (int*)malloc(sizeof(int) * n);
		Flag = (int*)malloc(sizeof(int) * n);

		if (S == NULL || Flag == NULL)
		{
			printf("Error!!\n");
			exit(-1);
		}

		for (i = 0; i < n; i++)
		    scanf("%d", &S[i]);
		

		DFS(S, Flag, n, 0, cnt);
		printf("\n");

		free(S);
		free(Flag);
	}
	return 0;
}

/*
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0


*/