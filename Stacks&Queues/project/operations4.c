#include "monty.h"

void op_rotl(stack_t **head, unsigned int line_number)
{
	stack_t *end = NULL, *second = NULL;
	(void)line_number;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return;

	end = *head;
	second = (*head)->next;

	while (end->next != NULL)
		end = end->next;

	end->next = *head;
	(*head)->prev = end;
	(*head)->next = NULL;

	second->prev = NULL;
	*head = second;
}

void op_rotr(stack_t **head, unsigned int line_number)
{
	stack_t *end = NULL, *second = NULL;
	int len = 0;
	(void)line_number;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return;

	end = *head;
	second = (*head)->next;

	while (end->next != NULL)
	{
		len++;
		end = end->next;
	}
	len++;

	if (len == 2)
		op_swap(head, 0);

	end->prev->next = *head;   // 2->0
	end->next = (*head)->prev; // 1->9
	(*head)->prev->prev = end // 1<-9
}
