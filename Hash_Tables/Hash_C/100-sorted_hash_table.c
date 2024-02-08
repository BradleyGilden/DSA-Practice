#include "hash_tables.h"

/**
 * shash_table_create - creates a hash table
 * @size: size of array (number of slots/buckets)
 * Return: address of newly created hashtable or NULL if failed
 */
shash_table_t *shash_table_create(unsigned long int size)
{
	shash_table_t *table = NULL;

	table = malloc(sizeof(shash_table_t));
	if (table == NULL)
		return (NULL);

	table->array = malloc(sizeof(shash_node_t *) * size);
	if (table->array == NULL)
	{
		free(table);
		return (NULL);
	}
	table->size = size;
	table->shead = NULL;
	table->stail = NULL;
	return (table);
}

/**
 * sorted - inserts new node in sorted list
 * @ht: pointer to hash table struct
 * @key: key used to access value
 * @cp: data stored in hash node
 * @hi: key index of hash table
 * Return: the built node or 0 if fails.
 */
int sorted(shash_table_t *ht, const char *key, char *cp, unsigned long int hi)
{
	shash_node_t *item = NULL, *hptr = NULL, *temp;

	item = malloc(sizeof(shash_node_t));
	if (item == NULL)
	{
		free(cp);
		return (0);
	}
	item->next = NULL, item->snext = NULL, item->sprev = NULL;
	item->value = cp, item->key = strdup(key);
	if (item->key == NULL)
	{
		free(cp);
		free(item);
		return (0);
	}
	item->next = ht->array[hi];
	ht->array[hi] = item;
	if (ht->shead == NULL)
		ht->shead = item, ht->stail = item;
	else if (strcmp(ht->shead->key, key) > 0)
	{
		item->snext = ht->shead;
		ht->shead->sprev = item;
		item->sprev = NULL;
		ht->shead = item;
	}
	else
	{
		hptr = ht->shead;
		while (hptr->snext != NULL && strcmp(hptr->key, key) < 0)
			hptr = hptr->snext;
		temp = hptr->snext, hptr->snext = item, item->sprev = hptr;
		item->snext = temp;
		if (temp != NULL)
			temp->sprev = item;
		else
			ht->stail = item;
	}
	return (1);
}

/**
 * shash_table_set - inserts hasnode into table slot or chain
 * @ht: pointer to hash table struct
 * @key: key used to access value
 * @value: data stored in hash node
 * Return: the built node or 0 if fails.
 */
int shash_table_set(shash_table_t *ht, const char *key, const char *value)
{
	shash_node_t *ptr = NULL;
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
	return (sorted(ht, key, value_copy, h_index));
}

/**
 * shash_table_get - Retrieve the value associated with
 *                   a key in a sorted hash table.
 * @ht: A pointer to the sorted hash table.
 * @key: The key to get the value of.
 *
 * Return: If the key cannot be matched - NULL.
 *         Otherwise - the value associated with key in ht.
 */
char *shash_table_get(const shash_table_t *ht, const char *key)
{
	shash_node_t *node;
	unsigned long int index;

	if (ht == NULL || key == NULL || *key == '\0')
		return (NULL);

	index = key_index((const unsigned char *)key, ht->size);
	if (index >= ht->size)
		return (NULL);

	node = ht->shead;
	while (node != NULL && strcmp(node->key, key) != 0)
		node = node->snext;

	return ((node == NULL) ? NULL : node->value);
}

/**
 * shash_table_print - Prints a sorted hash table in order.
 * @ht: A pointer to the sorted hash table.
 */
void shash_table_print(const shash_table_t *ht)
{
	shash_node_t *node;

	if (ht == NULL)
		return;

	node = ht->shead;
	printf("{");
	while (node != NULL)
	{
		printf("'%s': '%s'", node->key, node->value);
		node = node->snext;
		if (node != NULL)
			printf(", ");
	}
	printf("}\n");
}

/**
 * shash_table_print_rev - Prints a sorted hash table in reverse order.
 * @ht: A pointer to the sorted hash table to print.
 */
void shash_table_print_rev(const shash_table_t *ht)
{
	shash_node_t *node;

	if (ht == NULL)
		return;

	node = ht->stail;
	printf("{");
	while (node != NULL)
	{
		printf("'%s': '%s'", node->key, node->value);
		node = node->sprev;
		if (node != NULL)
			printf(", ");
	}
	printf("}\n");
}

/**
 * shash_table_delete - Deletes a sorted hash table.
 * @ht: A pointer to the sorted hash table.
 */
void shash_table_delete(shash_table_t *ht)
{
	shash_table_t *head = ht;
	shash_node_t *node, *tmp;

	if (ht == NULL)
		return;

	node = ht->shead;
	while (node)
	{
		tmp = node->snext;
		free(node->key);
		free(node->value);
		free(node);
		node = tmp;
	}

	free(head->array);
	free(head);
}
