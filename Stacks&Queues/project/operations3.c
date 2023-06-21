#include "monty.h"

void op_div(stack_t **head, unsigned int line_number)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
	{
		fprintf(stderr, "L%d: can't div, stack too short\n", line_number);
		free_tokens(optokens);
		exit(EXIT_FAILURE);
	}
    if ((*head)->n == 0)
    {
		fprintf(stderr, "L%d: division by zero\n", line_number);
		free_tokens(optokens);
		exit(EXIT_FAILURE);
    }
	(*head)->next->n =  (*head)->next->n / (*head)->n;
	op_pop(head, line_number);
}

void op_mul(stack_t **head, unsigned int line_number)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
	{
		fprintf(stderr, "L%d: can't mul, stack too short\n", line_number);
		free_tokens(optokens);
		exit(EXIT_FAILURE);
	}

	(*head)->next->n =  (*head)->next->n * (*head)->n;
	op_pop(head, line_number);
}

void op_mod(stack_t **head, unsigned int line_number)
{
	if (head == NULL || *head == NULL || (*head)->next == NULL)
	{
		fprintf(stderr, "L%d: can't mod, stack too short\n", line_number);
		free_tokens(optokens);
		exit(EXIT_FAILURE);
	}
    if ((*head)->n == 0)
    {
		fprintf(stderr, "L%d: division by zero\n", line_number);
		free_tokens(optokens);
		exit(EXIT_FAILURE);
    }
	(*head)->next->n =  (*head)->next->n % (*head)->n;
	op_pop(head, line_number);
}

void op_pchar(stack_t **head, unsigned int line_number)
