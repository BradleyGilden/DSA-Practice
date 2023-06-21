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
	int i = 0, value = 0, compare = 0;
	char *opcodes[15] = {"push", "pull", "pall", "pint", "add", "pop", "swap",
						"add", "nop", "sub", "div", "mul", "mod", "pchar",
						"pstr"};

	for (i = 0; i < 15; i++)
	{
		if (strcmp(optokens[0], opcodes[i]) == 0)
		{
			compare = strcmp("push", optokens[0]);
			if (glob->count == 1 && compare == 0)
				push_err(stack, glob);
			if (glob->count == 2)
			{
				value =_isdigit(optokens[1]);
				if (value == 0 && compare == 0)
					push_err(stack, glob);
			}
			return;
		}
	}

	fprintf(stderr, "L%d: unknown instruction %s\n", glob->l_num, optokens[0]);
	free_alloced(glob);
	fclose(glob->file);
	exit(EXIT_FAILURE);
}
