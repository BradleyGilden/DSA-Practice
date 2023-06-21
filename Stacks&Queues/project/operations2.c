#include "monty.h"

void op_pop(stack_t **head, unsigned int line_number)
{
	stack_t *temp;

    if (head == NULL || *head == NULL)
    {
        fprintf(stderr, "L%d: can't pop an empty stack\n", line_number);
        free_tokens(optokens);
        exit(EXIT_FAILURE);
    }

    temp = *head;
	*head = (*head)->next;
	free(temp);
	if (*head != NULL)
		(*head)->prev = NULL;
}
