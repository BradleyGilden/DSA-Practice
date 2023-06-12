#include "main.h"

/**
 * main - main entry point of program
 * Return: 0 always
 */

int main(void)
{
	int count = 0;
	list_t *head = NULL;

	head = add_end(head, "Henry", 48);  //pos 2
	add_end(head, "Larry", 52);  //pos 1
	add_end(head, "Constantine", 25);  //pos 0
	add_end(head, "Jerry", 2);  //pos 3
	add_end(head, "Wilder", 16); //pos 4
	
	//add_beg(&head, "Kyle", 20);
	//add_pos(&head, "Paulie", 22, 3);
	//del_pos(&head, 5);

	//del_beg(&head);
	//del_end(head);
	reverse(&head);
	count = count_nodes(head);
	print_nodes(head);
	printf("There are %d nodes\n", count);
	free_nodes(head);

	return (0);
}
