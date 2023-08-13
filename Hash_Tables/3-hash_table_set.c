#include "hash_tables.h"

/**
 * build_node - creates hash node with desired key and value
 * @key: key used to access value
 * @copy: copy of value
 * Return: the built node or NULL if fails.
 */
hash_node_t *build_node(const char *key, char *copy)
{
	hash_node_t *item = NULL;

	item = malloc(sizeof(hash_node_t));
	if (item == NULL)
	{
		free(copy);
		return (NULL);
	}

	item->key = strdup(key);
	if (item->key == NULL)
	{
		free(copy);
		free(item);
		return (NULL);
	}
	item->value = copy;
	item->next = NULL;
	return (item);
}

/**
 * hash_table_set - inserts hasnode into table slot or chain
 * @ht: pointer to hash table struct
 * @key: key used to access value
 * @value: data stored in hash node
 * Return: the built node or 0 if fails.
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	hash_node_t *item = NULL, *ptr = NULL;
	char *value_copy = NULL;
	unsigned long int h_index;

	if (ht == NULL || key == NULL || value == NULL || *key == '\0')
		return (0);

	value_copy = strdup(value);
	if (value_copy == NULL)
		return (0);

	h_index = key_index((unsigned char *)key, ht->size);
	ptr = ht->array[h_index];
	while (ptr != NULL)
	{
		if (strcmp(ptr->key, key) == 0)
		{
			free(ptr->value);
			ptr->value = value_copy;
			return (1);
		}
		ptr = ptr->next;
	}

	item = build_node(key, value_copy);
	if (item == NULL)
		return (0);
	if (ht->array[h_index] == NULL)
		ht->array[h_index] = item;
	else
	{
		/*ht->array[h_index] is techincally the head*/
		item->next = ht->array[h_index];
		ht->array[h_index] = item;
	}

	return (1);
}
