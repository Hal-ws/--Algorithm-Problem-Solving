#include <stdio.h>
#include <stdlib.h>


int main(void) {
	int N, B, num;
	int digit = 0;
	int i, asci;
	scanf_s("%d%d", &N, &B);
	// A: 65, Z= 90
	num = N;
	while (num > 0)
	{
		digit++;
		num = num / B;
	}
	char* answer = (char*)malloc(sizeof(char) * digit + 1);
	for (i = digit - 1; i >= 0; i--)
	{
		asci = N % B;
		if (asci >= 0 && asci <= 9)
			answer[i] = asci + 48;
		else
			answer[i] = asci + 55;
		N /= B;
	}
	answer[digit] = '\0';
	printf("%s\n", answer);
	return 0;
}
