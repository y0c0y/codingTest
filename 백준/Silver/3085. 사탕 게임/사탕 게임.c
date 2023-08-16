#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>

int check_row(char str[][51], int n);
int check_col(char str[][51], int n);


int main()
{
	char str[50][51] = { '\0' };
	char str_copy[50][51] = { '\0' };
	

	char temp = '\0';

	int n; //줄 수
	int i, j;
	int row = 0, col = 0;
	int max = 0;
	int r_max = 0, c_max = 0;
	int result = 0;
	int a = 0;


	scanf("%d", &n);
	getchar();

	for (i = 0; i < n; i++)
	{
		scanf("%s", str[i]);
		getchar();
	}
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n - 1; j++)
		{
			for (a = 0; a < n; a++)
			{
				strcpy(str_copy[a], str[a]);

			}
			if (str_copy[i][j] != str_copy[i][j + 1])
			{
				temp = str_copy[i][j];
				str_copy[i][j] = str_copy[i][j+1];
				str_copy[i][j + 1] = temp;
			}
			row = check_row(str_copy, n);
			col = check_col(str_copy, n);
			max = row > col ? row : col;
			r_max = max > r_max ? max : r_max;
		}
	}
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n - 1; j++)
		{
			for (a = 0; a < n; a++)
			{
				strcpy(str_copy[a], str[a]);

			}
			if (str_copy[j][i] != str_copy[j + 1][i])
			{
				temp = str_copy[j][i];
				str_copy[j][i] = str_copy[j + 1][i];
				str_copy[j + 1][i] = temp;
			}
			row = check_row(str_copy, n);
			col = check_col(str_copy, n);
			max = row > col ? row : col;
			c_max = max > c_max ? max : c_max;
		}
	}
	result = c_max > r_max ? c_max : r_max;
	printf("%d\n",result);
	return 0;
}

int check_row(char p[50][51], int n)
{
	int i, j;
	int cnt = 0, max = 0;


	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n - 1; j++)
		{
			if (p[i][j] == p[i][j + 1])
			{
				cnt++;

				if (j == n - 2 && p[i][n - 2] == p[i][n - 1])
				{
					cnt++;
					if (cnt > max)
					{
						max = cnt;
					}
					cnt = 0;
				}
			}
			if (p[i][j] != p[i][j + 1] )
			{
				if (j > 0 && p[i][j - 1] == p[i][j])
				{
					cnt++;


				}
				if (cnt > max)
				{
					max = cnt;
				}
				cnt = 0;
			}
		}
	}
	return max;
}

int check_col(char p[50][51], int n)
{
	int i, j;
	int cnt = 0, max = 0;

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n - 1; j++)
		{
			if (p[j][i] == p[j + 1][i])
			{
				cnt++;

				if (j == n - 2 && p[n - 2][i] == p[n - 1][i])
				{
					cnt++;
					if (cnt > max)
					{
						max = cnt;

					}
					cnt = 0;

				}
			}
			if (p[j][i] != p[j + 1][i])
			{
				if (j > 0 && p[j - 1][i] == p[j][i])
				{
					cnt++;
				}
				if (cnt > max)
				{
					max = cnt;
				}
				cnt = 0;

			}

		}
	}
	return max;
}
