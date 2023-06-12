#include "main.h"

/**
 * del_beg - deletes beginning of linked list
 * @head: head node
 */
void del_beg(list_t **head)
{
	list_t *ptr = *head;

	if (head == NULL || *head == NULL)
		return;
		
	*head = (*head)->next;
	free(ptr->name);
	free(ptr);
}
