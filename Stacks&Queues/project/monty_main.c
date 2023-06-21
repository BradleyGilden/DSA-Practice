#include "monty.h"

char **optokens = NULL;

/**
 * main - Entry point
 * @argc: arg count
 * @argv: arg vector
 * Return: 0 always
 */

int main(int argc, char *argv[])
{
	globals_t glob = {NULL, NULL, NULL, 0, 0};
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
		glob.l_num += 1;
		validate_opcode(&glob, file);
		if (glob.count == 2)
			printf("%s    %s\n", optokens[0], optokens[1]);
		else if(glob.count == 1)
			printf("%s\n", optokens[0]);
		free_alloced(&glob);
	}
	if (glob.line != NULL)
		free(glob.line);
	fclose(file);
}
