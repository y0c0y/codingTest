#pragma warning(disable:4996)
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct
{
	int* importance;
	int* index;
	int front, rear;
}Queue;
typedef struct
{
	int importance;
	int index;
}ImpAndInd;
Queue* createQueue(int Qsize)
{
	Queue* Q;
	Q = (Queue*)malloc(sizeof(Queue));
	Q->importance = (int*)malloc(sizeof(int) * Qsize);
	Q->index = (int*)malloc(sizeof(int) * Qsize);
	if (Q == NULL || Q->importance == NULL || Q->index == NULL) exit(-1);
	Q->front = -1;
	Q->rear = -1;
	return Q;
}
int isEmpty(Queue* Q)
{
	if (Q->front == Q->rear) return 1;
	return 0;
}
int isFull(Queue* Q, int Qsize)
{
	if (Q->rear == Qsize) return 1;
	return 0;
}
int determineImport(Queue* Q, int Qsize)
{	
	for (int i = Q->front + 1; i < Qsize; i++)
		if (Q->importance[Q->front + 1] < Q->importance[i]) return 1;
	return 0;
}
void enQueue(Queue* Q, int item, int index, int Qsize)
{
	if (isFull(Q, Qsize)) exit(-1);	
	else
	{
		Q->rear++;
		Q->importance[Q->rear] = item;
		Q->index[Q->rear] = index;
	}
}
void moveQueue(Queue* Q, int Qsize)
{
	ImpAndInd tmp;
	tmp.importance = Q->importance[Q->front + 1];
	tmp.index = Q->index[Q->front + 1];
	for (int i = Q->front + 1; i < Q->rear; i++)
	{
		Q->importance[i] = Q->importance[i + 1];
		Q->index[i] = Q->index[i + 1];
	}
	Q->importance[Q->rear] = tmp.importance;
	Q->index[Q->rear] = tmp.index;
}
ImpAndInd deQueue(Queue* Q, int Qsize)
{
	ImpAndInd tmp;
	if (isEmpty(Q)) exit(-1);	
	else
	{
		Q->front++;
		tmp.importance = Q->importance[Q->front];
		tmp.index = Q->index[Q->front];
		return tmp;
	}
}
int main()
{
	Queue* Q;
	ImpAndInd tmp;
	int Qsize, find, cnt = 0;
	int num, item;
	int i, j;
	scanf("%d", &num);
	for (i = 0; i < num; i++)
	{
		scanf("%d %d", &Qsize, &find);
		Q = createQueue(Qsize);
		for (j = 0; j < Qsize; j++)
		{
			scanf("%d", &item);
			enQueue(Q, item, j, Qsize);
		}
		tmp.index = -1;
		while (find != tmp.index)
		{
			if (determineImport(Q, Qsize)) moveQueue(Q, Qsize);
			else
			{
				cnt++;
				tmp = deQueue(Q, Qsize);
			}
		}
		printf("%d\n", cnt);
		free(Q->importance);
		free(Q->index);
		free(Q);
		cnt = 0;
	}
	return 0;
}