#include "monty.h"
#include <stdlib.h>

void malloc_fail(char *line, globals_t *glob)
{
	if (line == NULL)
	{
		free_alloced(glob);
		fprintf(stderr, "Error: malloc failed\n");
		fclose(glob->file);
		exit(EXIT_FAILURE);
	}
	
}

void dmalloc_fail(char **tokarr, globals_t *glob)
{
	if (tokarr == NULL)
	{
		free_alloced(glob);
		fprintf(stderr, "Error: malloc failed\n");
		fclose(glob->file);
		exit(EXIT_FAILURE);
	}
}
void checkargs(int ac)
{
	if (ac != 2)
	{
		fprintf(stderr, "USAGE: monty file\n");
		exit(EXIT_FAILURE);
	}
}

void checkstream(FILE *file, char *filename)
{
	if (file == NULL)
	{
		fprintf(stderr, "Error: Can't open file %s\n", filename);
		exit(EXIT_FAILURE);
	}
}

void validate_opcode(globals_t *glob, stack_t *stack)
{
	int i = 0;
	int value = 0;
	int compare = 0;
	char *opcodes[9] = {"push", "pull", "pall",
						"pint", "add", "pop",
						"swap", "add", "nop"};

	for (i = 0; i < 9; i++)
	{
		if (strcmp(optokens[0], opcodes[i]) == 0)
		{
			if (glob->count == 2)
			{
				value =_isdigit(optokens[1]);
				compare = strcmp("push", optokens[0]);
				if (value == 0 && compare == 0 ||
				glob->count == 1 && compare == 0)
				{
					fprintf(stderr, "L%d: usage: push integer\n", glob->l_num);
					free_list(stack);
					free_alloced(glob);
					fclose(glob->file);
					exit(EXIT_FAILURE);
				}
			}
			return;
		}
	}

	fprintf(stderr, "L%d: unknown instruction %s\n", glob->l_num, optokens[0]);
	free_alloced(glob);
	fclose(glob->file);
	exit(EXIT_FAILURE);
}
