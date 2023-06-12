#include "main.h"

/**
 * free_nodes - frees a linked list
 * @head: head node
 */

void free_nodes(list_t *head)
{
	list_t *prev;

	while(head != NULL)
	{
		prev = head;
		head = head->next;
		free(prev->name);
		free(prev);
	}
}

