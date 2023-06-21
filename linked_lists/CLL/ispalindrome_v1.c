#include "main.h"

/**
 * llen - checks length of linked list
 * @head: head node of linked list
 * Return: length of linked list
 */
int count_nodes(list_t *head)
{
	int len = 0;

	while (head != NULL)
	{
		head = head->next;
		len++;
	}
	return (len);
}

/**
 * alloc - stores data from linked list in an array
 * @head: head node of linked list
 * @len: length of linked list
 * Return: returns alloced array, NULL if failed
 */
int *alloc(list_t *head, int len)
{
	int *arr, i = 0;

	arr = malloc(sizeof(int) * len);

	if (arr == NULL)
		return (NULL);

	while (head != NULL)
	{
		arr[i++] = head->age;
		head = head->next;
	}

	return (arr);
}

/**
 * is_palindrome - checks if linked list data is a palindrome
 * @head: head node of linked list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(list_t **head)
{
	int *arr;
	int len, i;

	len = count_nodes(*head);
	if (len == 0)
		return (1);

	arr = alloc(*head, len);
	if (arr == NULL)
		return (0);

	for (i = 0; i < len / 2; i++)
	{
		if (arr[i] != arr[len - i - 1])
		{
			free(arr);
			return (0);
		}	
	}

	free(arr);
	return (1);
}

