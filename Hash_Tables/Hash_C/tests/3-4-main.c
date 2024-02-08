#include "../hash_tables.h"

/**
 * main - check the code
 *
 * Return: Always EXIT_SUCCESS.
 */
int main(void)
{
    hash_table_t *ht;
    char *value;

    ht = hash_table_create(1024);
    hash_table_set(ht, "c", "fun");
    hash_table_set(ht, "python", "awesome");
    hash_table_set(ht, "Bob", "and Kris love asm");
    hash_table_set(ht, "N", "queens");
    hash_table_set(ht, "Asterix", "Obelix");
    hash_table_set(ht, "Betty", "Cool");
    hash_table_set(ht, "98", "Battery Street");
    hash_table_set(ht, "c", "isfun");
    hash_table_set(ht, "Hunger Games", "Catching Fire");
    hash_table_set(ht, "Hunger Games", "Mocking Jay");
	hash_table_set(ht, "hetairas", "aguamenti");
	hash_table_set(ht, "mentioner", "petrificus totalus");

    value = hash_table_get(ht, "python");
    printf("%s:   \t%s\n", "python", value);
    value = hash_table_get(ht, "Bob");
    printf("%s:     \t%s\n", "Bob", value);
    value = hash_table_get(ht, "N");
    printf("%s:        \t%s\n", "N", value);
    value = hash_table_get(ht, "Asterix");
    printf("%s:   \t%s\n", "Asterix", value);
    value = hash_table_get(ht, "Betty");
    printf("%s:    \t%s\n", "Betty", value);
    value = hash_table_get(ht, "98");
    printf("%s:       \t%s\n", "98", value);
    value = hash_table_get(ht, "c");
    printf("%s:       \t%s\n", "c", value);
    printf("%s:\t%s\n", "Hunger Games", hash_table_get(ht, "Hunger Games"));
	printf("%s:\t%s\n", "hetairas", hash_table_get(ht, "hetairas"));
	printf("%s:\t%s\n", "mentioner", hash_table_get(ht, "mentioner"));
    value = hash_table_get(ht, "javascript");
    printf("%s:\t%s\n", "javascript", value);
    return (EXIT_SUCCESS);
}
