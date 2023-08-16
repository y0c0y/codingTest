#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int input_ind = 0;

void inorder(int* tree, int* input, int tree_ind, int size)
{
	if (tree_ind > size)
	{
		return;
	}

	inorder(tree, input, tree_ind * 2,  size);
	tree[tree_ind] = input[input_ind - 1];
	input_ind++;
	inorder(tree, input, tree_ind * 2 + 1,size);
}

int main()
{
	int* tree;
	int* input;

	int k;
	int size = 1;
	int i;

	scanf("%d", &k);

	for (i = 0; i < k; i++)
	{
		size *= 2;
	}

	tree = (int*)malloc(sizeof(int) * size);
	input = (int*)malloc(sizeof(int) * (size - 1));

	if (tree == NULL || input == NULL)
	{
		exit(-1);
	}

	for (i = 0; i < size - 1; i++)
	{
		scanf("%d", &input[i]);
	}
	
	inorder(tree, input, 1,size);
	
	k = 1;

	for (i = 1; i < size; i++)
	{
		printf("%d ", tree[i]);
		if (i == k)
		{
			printf("\n");
			k = k * 2 + 1;
		}
	}

	return 0;
}

/*

*/