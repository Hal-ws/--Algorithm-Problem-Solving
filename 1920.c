#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int compare(const void* a, const void* b)
{
	if (*(int*)a > *(int*)b)
		return 1;
	else if (*(int*)a < *(int*)b)
		return -1;
	else
		return 0;
}


int bSearch(int arr[], int num, int l)
{
	int left, right, mid;
	left = 0;
	right = l - 1;
	while (left <= right)
	{
		mid = (left + right) / 2;
		if (arr[mid] == num)
			return 1;
		else
		{
			if (arr[mid] > num)
				right = mid - 1;
			else
				left = mid + 1;
		}
	}
	return 0;
}


int main(void) {
	int N, M;
	scanf_s("%d", &N);
	int* nList = (int*)malloc(sizeof(int) * N);
	for (int i = 0; i < N; i++)
		scanf_s("%d", &nList[i]);
	qsort(nList, N, sizeof(nList[0]), compare);
	scanf_s("%d", &M);
	int* fList = (int*)malloc(sizeof(int) * M);
	for (int i = 0; i < M; i++)
		scanf_s("%d", &fList[i]);
	for (int i = 0; i < M; i++)
		printf("%d\n", bSearch(nList, fList[i], N));
	return 0;
}
