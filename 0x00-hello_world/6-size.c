#include <stdio.h>
/**
 * main - print sizes of data types
 *
 * Return: 0
*/

int main(void)
{

	printf("size of char: %lu byte(S)\n", (unsigned long)sizeof(char));
	printf("size of int: %lu byte(S)\n", (unsigned long)sizeof(int));
	printf("size of long int: %lu byte(S)\n", (unsigned long)sizeof(long int));
	printf("size of long long int: %lu byte(S)\n", (unsigned long)sizeof(long long int));
	printf("size of float: %lu byte(S)\n", (unsigned long)sizeof(float));
	return (0);

}
