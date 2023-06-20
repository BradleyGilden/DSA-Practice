#include "monty.h"

char **optokens = NULL;


/**
 * main - Entry point
 * @argc: arg count
 * @argv: arg vector
 * Return: 0 always
 */



void free_tokens(char **tokarr)
{
	int i = 0, len = 0;

	if (tokarr == NULL)
		return;

	while (tokarr[i++])
	{
		len++;
	}

	for (i = len - 1; i >= 0; i--)
		free(tokarr[i]);

	free(tokarr);
}

void free_alloced(globals_t *glob)
{
	if (glob->line != NULL)
		free(glob->line);
	if (glob->tokarr != NULL)
		free_tokens(glob->tokarr);
	if (glob->copy != NULL)
		free(glob->copy);
	glob->line = NULL, glob->copy = NULL, glob->tokarr = NULL;
}



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

char **get_tokens(globals_t *glob)
{
	char *delim = "\v\t\n ";
	char *token = NULL;
	unsigned int count = 1, i;

	glob->copy = strdup(glob->line);
	if (glob->copy == NULL)
		malloc_fail(glob->copy, glob);

	token = strtok(glob->copy, delim);
	if (token == NULL)
	{
		free_alloced(glob);
		return (NULL);
	}

	count++;
	token = strtok(NULL, delim);
	if (token != NULL)
		count++;
	glob->count = count -1;
	glob->tokarr = malloc(sizeof(char *) * count);
	if (glob->tokarr == NULL)
		dmalloc_fail(glob->tokarr, glob);

	token = strtok(glob->line, delim);
	for (i = 0; token != NULL; i++)
	{
		glob->tokarr[i] = malloc(sizeof(char) * (strlen(token) + 1));
		if (glob->tokarr[i] == NULL)
			malloc_fail(glob->line, glob);

		strcpy(glob->tokarr[i], token);
		token = strtok(NULL, delim);
	}
	glob->tokarr[i] = NULL;
	return (glob->tokarr);
}

int main(int argc, char *argv[])
{
	globals_t glob = {NULL, NULL, NULL, 0};
	char *filename;
	size_t n = 0;
	ssize_t ret = 0;

	checkargs(argc);
	filename = argv[1];

	FILE *file = fopen(filename, "r");

	checkstream(file, filename);

	while ((ret = getline(&(glob.line), &n, file)) >= 0)
	{
		if (ret == 0)
			continue;
		optokens = get_tokens(&glob);
		if (optokens == NULL)
			continue;
		if (glob.count == 2)
			printf("%s    %s\n", optokens[0], optokens[1]);
		else if(glob.count == 1)
			printf("%s\n", optokens[0]);
		free_alloced(&glob);
	}
	free(glob.line);
	fclose(file);
}
