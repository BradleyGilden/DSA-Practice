#include "main.h"

/**
 * del_end - deletes the end of a linked list
 * @head: head node
 */
void del_end(list_t *head)
{
	list_t *prev = NULL;

	if (head == NULL)
		return;
	while (head->next != NULL)
	{
		prev = head;
		head = head->next;
	}
	prev->next = NULL;
	free(head->name);
	free(head);
}
