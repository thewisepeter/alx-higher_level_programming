#include "lists.h"

/**
 * insert_node -  that inserts a number into a
 * sorted singly linked list
 * @head: double pointer to first node
 * @number: integer to insert
 *
 * Return: pointer to new node (success) NULL (fail)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	if (node == NULL || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}
