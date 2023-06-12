#include "main.h"

/**
 * add_end - add's node at end of the list
 * @head: head node
 * @name: persons name
 * @age: persons age
 * Return: address of new_node or head node if list is empty
 */

list_t *add_end(list_t *head, char *name, int age)
{
	list_t *new_node;

	if (head == NULL)
	{
		head = add_beg(&head, name, age);
		return (head);
	}

	new_node = malloc(sizeof(list_t));
	
	if (new_node == NULL)
		return (NULL);

	new_node->age = age;
	new_node->name = strdup(name);
	new_node->next = NULL;

	while (head->next != NULL)
		head = head->next;
	head->next = new_node;

	return(new_node);
}
