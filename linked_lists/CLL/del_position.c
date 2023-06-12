#include "main.h"

/**
 * del_beg - deletes node at index pos in linked list
 * @head: head node
 * pos: position of node to be deleted starting from 0
 */
void del_pos(list_t **head, int pos)
{
	int len = count_nodes(*head);
	int tracker = 1;
	list_t *prev = NULL;
	list_t *after = NULL;
	list_t *ptr = *head;

	if (head == NULL || *head == NULL)
		return;

	if (pos > len - 1)
		printf("Index out of range\n");
	else if (pos == 0)
		del_beg(head);
	else if (pos == len - 1)
		del_end(*head);
	else
	{
		after = ptr->next;
		while(ptr->next != NULL)
		{
			if (tracker == pos)
			{
				prev = ptr;
				ptr = ptr->next;
				after = after->next;
				free(ptr->name);
				free(ptr);
				prev->next = after;
			}
			tracker += 1;
			ptr = ptr->next;
			after = after->next;
		}
	}
}
