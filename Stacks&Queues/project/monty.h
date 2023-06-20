#ifndef _MONTY_H_
#define _MONTY_H_

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern char **optokens;

typedef struct globals
{
	char **tokarr;
	char *line;
	char *copy;
	int count;
} globals_t;

/**
 * struct stack_s - doubly linked list representation of a stack (or queue)
 * @n: integer
 * @prev: points to the previous element of the stack (or queue)
 * @next: points to the next element of the stack (or queue)
 *
 * Description: doubly linked list node structure
 * for stack, queues, LIFO, FIFO
 */
typedef struct stack_s
{
	int n;
	struct stack_s *prev;
	struct stack_s *next;
} stack_t;

/**
 * struct instruction_s - opcode and its function
 * @opcode: the opcode
 * @f: function to handle the opcode
 *
 * Description: opcode and its function
 * for stack, queues, LIFO, FIFO
 */
typedef struct instruction_s
{
	char *opcode;
	void (*f)(stack_t **stack, unsigned int line_number);
} instruction_t;

void free_tokens(char **tokarr);
void free_alloced(globals_t *glob);
void malloc_fail(char *line, globals_t *glob);
void dmalloc_fail(char **tokarr, globals_t *glob);
void checkargs(int ac);
void checkstream(FILE *file, char *filename);
char **get_tokens(globals_t *glob);

#endif /*_MONTY_H_*/
