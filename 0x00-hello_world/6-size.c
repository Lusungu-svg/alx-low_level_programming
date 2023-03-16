#include <stdio.h>
/**
 * main - print sizes of data types
 *
 * Return: 0
*/

int main(void)
{

	printf("size of char: %ld bytes\n", sizeof(char));
	printf("size of int: %ld bytes\n", sizeof(int));
	printf("size of long int: %ld bytes\n", sizeof(long int));
	printf("size of long long int: %ld bytes\n", sizeof(long long int));
	printf("size of float: %ld bytes\n", sizeof(float));
	return (0);

}
