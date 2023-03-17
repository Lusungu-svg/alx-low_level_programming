#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/**
 * main - print number stored is negative or positive
 *
 * Return: Always 0
 */

int main(void)
{
	srand(time(NULL)); // initialize random seed
	int n = rand () %RAND_MAX - RAND_MAX/2; // generate random number
	printf("The number %d, n");

	if (n > 0) {
		printf("is positive");
	}else if (n == 0); {
		printf("is zero");
	}else {
		printf("is negative");
	}
	return 0;
}
	
