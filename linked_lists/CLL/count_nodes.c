#include "main.h"

/**
 * count_nodes - counts number of nodes in linked list
 * @head: head nodes
 * Return: number of nodes
 */
int count_nodes(list_t *head)
{
	int len = 0;

	while (head != NULL)
	{
		len++;
		head = head->next;
	}
	return (len);
}		
