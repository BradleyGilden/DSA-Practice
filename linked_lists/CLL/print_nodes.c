#include "main.h"

/**
 * print_nodes - print_nodes in a linked list
 * @head: head node
 */
void print_nodes(list_t *head)
{
	while (head != NULL)
	{
		printf("Name:%s\tAge:%d\n", head->name, head->age);
		head = head->next;
	}
}
