#include "monty.h"

void malloc_fail(char *line, globals_t *glob)
{
	if (line == NULL)
	{
		free_alloced(glob);
		fprintf(stderr, "Error: malloc failed\n");
		exit(EXIT_FAILURE);
	}
	
}

void dmalloc_fail(char **tokarr, globals_t *glob)
{
	if (tokarr == NULL)
	{
		free_alloced(glob);
		fprintf(stderr, "Error: malloc failed\n");
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
