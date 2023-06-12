#include "main.h"

/**
 * add_pos - add's node at index pos starting from 0
 * @head: head node
 * @name: persons name
 * @age: persons age
 * @pos: position to add node
 * Return: address of new node or head node if list is empty
 */
list_t *add_pos(list_t **head, char *name, int age, int pos)
{
	int tracker = 1;
	int len = count_nodes(*head);
	list_t *new_node, *temp, *ptr = *head;

	if (head == NULL || *head == NULL || pos == 0)
	{
		*head = add_beg(head, name, age);
		return (*head);
	}
	if (pos > len-1)
	{
		new_node = add_end(*head, name, age);
		return (new_node);
	}
	new_node = malloc(sizeof(list_t));
	if (new_node == NULL)
		return (NULL);
	new_node->age = age;
	new_node->name = strdup(name);
	new_node->next = NULL;
	while (ptr->next != NULL)
	{
		temp = ptr->next;
		if (tracker == pos)
		{
			ptr->next = new_node;
			new_node->next = temp;
			return (new_node);
		}
		ptr = ptr->next;
		tracker++;
	}
	return (new_node);
}
