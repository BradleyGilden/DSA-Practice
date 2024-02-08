#include "../hash_tables.h"

/**
 * main - check the code
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    char *s;
    unsigned long int h_code;

    printf("Array size: 1024\n\n");

    s = "cisfun";
    h_code = hash_djb2((unsigned char *)s);
    printf("%lu, array index = %lu\n", h_code, h_code % 1024);

    s = "Don't forget to tweet today";
    h_code = hash_djb2((unsigned char *)s);
    printf("%lu, array index = %lu\n", h_code, h_code % 1024);

    s = "98";
    h_code = hash_djb2((unsigned char *)s);
    printf("%lu, array index = %lu\n", h_code, h_code % 1024);

    printf("\n");
    printf("Showing possible collison\n");
    printf("\n");

    s = "hetairas";
    h_code = hash_djb2((unsigned char *)s);
    printf("%lu, array index = %lu\n", h_code, h_code % 1024);

    s = "mentioner";
    h_code = hash_djb2((unsigned char *)s);
    printf("%lu, array index = %lu\n", h_code, h_code % 1024);
    return (EXIT_SUCCESS);
}
