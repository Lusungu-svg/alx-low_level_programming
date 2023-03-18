#include <stdlib.h>
#include <time.h>
#include <stdio.h>
/**
 * main - print tha last digit of the num stored variable
 *
 * Return: 0
 */
int main(void)
{
	int n;
	int x;

	srand(time(0));
	n = rand() - RAND_MAX / 2;
	x = n % 10;
	printf("Last digit of %d is %d", n, x);
	if (x > 5)
	{
		printf("and is greater than 5");
	}
	if else(x == 0)
		printf("and is 0");
	{
	else
		printf("and is less than 6 and not 0");
	}
	return (0);
}
