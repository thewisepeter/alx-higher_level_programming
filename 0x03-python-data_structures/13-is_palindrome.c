#include "lists.h"

/**
 * reverse_listint - function that reverses a linked list
 * @head: linked list
 *
 * Return: pointer to reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (*head);

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if list is a palindrome
 * @head: linked list
 *
 * Return: 1 (success) 0 (fail)
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *split = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			split = slow->next;
			break;
		}
		if (!fast->next)
		{
			split = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&split);

	while (split && temp)
	{
		if (temp->n == split->n)
		{
			split = split->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!split)
		return (1);

	return (0);
}
