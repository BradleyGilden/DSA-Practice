#include "main.h"
/**
 * reverse - reverses linked list
 * @head: head node
 */

void reverse(list_t **head)
{
	list_t *after = NULL, *prev = NULL;
	int len = (count_nodes(*head));
	
	if (len == 0 || len == 1)
		return;

	while (*head != NULL)
	{
		after = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = after;
	}

	*head = prev;
}
