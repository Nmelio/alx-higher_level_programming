#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted singly linked list
 *
 * @head: pointer to head of linked list
 * @number: number to be inserted
 *
 * Return: NULL or pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
