#include "hash_tables.h"

/**
 * hash_table_print - print hash table with format: {key: value}
 * @ht: pointer to hash table struct
 */
void hash_table_print(const hash_table_t *ht)
{
	hash_node_t *ptr = NULL;
	unsigned int i, max_index;

	if (ht == NULL)
		return;

	/*start*/
	printf("{");

	for (i = 0; i < ht->size; i++)
	{
		if (ht->array[i] != NULL)
			max_index = i;
	}

	for (i = 0; i < ht->size; i++)
	{
		ptr = ht->array[i];
		while (ptr != NULL)
		{
			if (i != max_index)
				printf("'%s': '%s', ", ptr->key, ptr->value);
			else
				printf("'%s': '%s'", ptr->key, ptr->value);
			ptr = ptr->next;
		}
	}
	printf("}\n");
}
