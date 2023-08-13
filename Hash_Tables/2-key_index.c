#include "hash_tables.h"

/**
 * key_index - converts hash code to array index
 * @size: size of array (number of slots/buckets)
 * @key: key to be indexed
 * Return: index of key entered
 */
unsigned long int key_index(const unsigned char *key, unsigned long int size)
{
	unsigned long int code = hash_djb2(key);

	return (code % size);
}
