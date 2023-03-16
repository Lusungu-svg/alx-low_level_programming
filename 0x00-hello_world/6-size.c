#include <stdio.h>

/**
 * main - prints out the sizes of data types
 * @void: Indicate no parameter
 *
 * Return: Returns 0
*/

int main(void)
{
	char a;
	int b;
	long int c;
	long long int d;
	float e;

	printf("size of a char: %d byte(S)\n", sizeof(a));
	printf("size of an int: %d byte(S)\n", sizeof(b));
	printf("size of a long int: %d byte(S)\n", sizeof(c));
	printf("size of a long long int: %d byte(S)\n", sizeof(d));
	printf("size of a float: %d byte(S)\n", sizeof(e));
	return (0);

}
