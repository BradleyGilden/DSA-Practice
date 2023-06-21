#include "monty.h"

void (*get_ops(char *opcode))(stack_t **stack, unsigned int line_number)
{
	int i = 0;
	instruction_t functions[] = {
		{"push", op_push},
		{"pall", op_pall},
		{"pint", op_pint},
		{"pop", op_pop},
		{"swap", op_swap},
		{"add", op_add},
		{"nop", op_nop},
        {"sub", op_sub},
        {"div", op_div},
        {"mul", op_mul},
        {"mod", op_mod},
        {"pchar", op_pchar},
        {"pstr", op_pstr},
		{"rotl", op_rotl},
		{NULL, NULL}
	};

	for (i = 0; functions[i].opcode; i++)
	{
		if (strcmp(optokens[0], functions[i].opcode) == 0)
			return (functions[i].f);
	}
    return (NULL);
}

void op_push(stack_t **head, unsigned int line_number)
{
	stack_t *new_node = malloc(sizeof(stack_t));
    int n;
    (void)line_number;

	if (new_node == NULL)
	{
        free_list(*head);
        free_tokens(optokens);
        fprintf(stderr, "Error: malloc failed\n");
        exit(EXIT_FAILURE);
    }
    n = atoi(optokens[1]);
	new_node->n = n;
	new_node->prev = NULL;
	if (*head == NULL)
	{
		new_node->next = NULL;
	}
	else
	{
		new_node->next = *head;
		(*head)->prev = new_node;
	}
	*head = new_node;
}

void free_list(stack_t *head)
{
	stack_t *temp;

	while (head != NULL)
	{
		temp = head;
		head = head->next;
		free(temp);
	}
}

void op_pall(stack_t **head, unsigned int line_number)
{
    stack_t *ptr = *head;
    (void)line_number;

	while (ptr != NULL)
	{
		printf("%d\n", ptr->n);
		ptr = ptr->next;
	}
}

void op_pint(stack_t **head, unsigned int line_number)
{
    if (head == NULL || *head == NULL)
    {
        fprintf(stderr, "L%d: can't pint, stack empty\n", line_number);
        free_tokens(optokens);
        exit(EXIT_FAILURE);
    }

    printf("%d\n", (*head)->n);
}
