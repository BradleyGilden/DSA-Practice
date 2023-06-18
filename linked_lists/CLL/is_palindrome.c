#include "lists.h"

/**
 * reverse - reverses linked list
 * @head: head node
 */
void reverse(listint_t **head)
{
	listint_t *after = NULL, *prev = NULL;
	int len = llen(*head);

	if (len == 0 || len == 1)
		return;

	while (*head != NULL)
	{
		after = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = after;
	}

	*head = prev;
}

/**
 * llen - checks length of linked list
 * @head: head node of linked list
 * Return: length of linked list
 */
int llen(listint_t *head)
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
 * is_palindrome - checks if linked list data is a palindrome
 * @head: head node of linked list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr, *ptr2 = NULL, *temp;
	int len;
	int half, count = 1;

	if (head == NULL || *head == NULL)
		return (1);
	len = llen(*head);
	if (len == 1)
		return (1);
	ptr = *head;
	half = len / 2;
	while (ptr != NULL)
	{
		if (count == half)
		{
			ptr2 = ptr->next;
			ptr->next = NULL;
			break;
		}
		ptr = ptr->next;
		count++;
	}
	ptr = *head;
	reverse(&ptr2);
	temp = ptr2;
	while (ptr != NULL || temp != NULL)
	{
		if (ptr->n != temp->n)
			return (0);
		ptr = ptr->next;
		temp = temp->next;
	}
	ptr = *head;
	reverse(&ptr2);
	while (ptr->next != NULL)
	{
		ptr = ptr->next;
	}
	ptr->next = ptr2;
	return (1);
}
