#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void QuadTree(int** arr, int n)
{

	int** S[4];
	int check[4] = { 0 };

	int s_x = 0, e_x = n / 2, s_y = 0, e_y = n / 2;
	int x, y;
	int i, j, k;

	int judge = 0, flag = 0;

	printf("(");

	if (n == 1)
	{
		printf("%d", arr[0][0]);
	}
	else
	{
		for (k = 0; k < 4; k++)
		{
			S[k] = (int**)malloc(sizeof(int*) * (n / 2));
			for (i = 0, y = s_y; y < e_y; i++, y++)
			{
				S[k][i] = (int*)malloc(sizeof(int) * (n / 2));

				judge = arr[s_y][s_x];

				for (j = 0, x = s_x; x < e_x; j++, x++)
				{
					S[k][i][j] = arr[y][x];

					if (judge != S[k][i][j] && flag == 0)
					{
						flag = 1;
					}
				}
			}

			if (flag == 1)
			{
				QuadTree(S[k], n / 2);
			}
			else
			{
				printf("%d", S[k][0][0]);
			}

			if (k == 0)
			{
				s_x = n / 2;
				e_x = n;
			}
			if (k == 1)
			{
				s_x = 0;
				e_x = n / 2;
				s_y = n / 2;
				e_y = n;
			}
			if (k == 2)
			{
				s_x = n / 2;
				e_x = n;
				s_y = n / 2;
				e_y = n;
			}

			flag = 0;
		}
	}

	printf(")");
}

int main()
{
	int** arr = NULL;
	int n, x, y, judge = 0, flag = 0;

	char com = '\0';

	scanf("%d", &n);
	getchar();


	arr = (int**)malloc(sizeof(int*) * n);
	if (arr == NULL)
	{
		printf("ERROR!!!!!\n");
		exit(-1);
	}

	for (y = 0; y < n; y++)
	{
		arr[y] = (int*)malloc(sizeof(int) * n);
		if (arr[y] == NULL)
		{
			printf("ERROR!!!!!\n");
			exit(-1);
		}

		for (x = 0; x < n; x++)
		{
			scanf("%c", &com);
			arr[y][x] = com - '0';
		}
		getchar();
	}

	for (y = 0; y < n; y++)
	{
		judge = arr[0][0];

		for (x = 0; x < n; x++)
		{
			if (judge != arr[y][x])
			{
				flag = 1;
			}
		}
	}

	if (flag != 0)
	{
		QuadTree(arr, n);
	}
	else
	{
		printf("%d", arr[0][0]);

	}


	return 0;
}

/*

1
1

4
1111
1111
1111
1111



8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011

8
00000000
00000000
00001111
00001111
00011111
00111111
00111111
00111111

*/
