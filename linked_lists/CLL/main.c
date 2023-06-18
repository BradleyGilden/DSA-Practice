#include "main.h"

/**
 * main - main entry point of program
 * Return: 0 always
 */

int main(void)
{
	int count = 0;
	list_t *head = NULL;
	list_t *loop = NULL;

	head = add_end(head, "Henry", 48);  //pos 2
	add_end(head, "Larry", 52);  //pos 1
	add_end(head, "Constantine", 25);  //pos 0
	add_end(head, "Jerry", 2);  //pos 3
	loop = add_end(head, "Wilder", 16); //pos 4

	is_cyclic(head);
	loop->next = head;
	is_cyclic(head);
	return (0);
}
