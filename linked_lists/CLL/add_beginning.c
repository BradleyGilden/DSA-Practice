#include "main.h"

list_t *add_beg(list_t **head, char *name, int age)
{
	list_t *new_node;

	if (head == NULL || *head == NULL)
	{
		*head = malloc(sizeof(list_t));
		if (*head == NULL)
			return (NULL);
		(*head)->name = strdup(name);
		if ((*head)->name == NULL)
			return (NULL);
		(*head)->age = age;
		(*head)->next = NULL;
		return (*head);
	}

	new_node = malloc(sizeof(list_t));
	if (new_node == NULL)
		return (NULL);
	new_node->name = strdup(name);
	if (new_node->name == NULL)
		return (NULL);
	new_node->age = age;
	new_node->next = *head;
	*head = new_node;
	return (*head);
}
