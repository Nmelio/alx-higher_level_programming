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
	listint_t *temp = *head;
	listint_t *current;

	current = malloc(sizeof(listint_t));
	if (current == NULL)
		return (NULL);
	current->n = number;

	if (temp == NULL || temp->n >= number)
	{
		current->next = temp;
		*head = current;
		return (current);
	}

	while (temp->next && temp->next->n < number && temp)
	{
		temp = temp->next;
	}

	current->next = temp->next;
	temp->next = current;

	return (current);
}
