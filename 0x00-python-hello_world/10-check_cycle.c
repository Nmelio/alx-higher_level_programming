#include "lists.h"

/**
 * check_cycle - funct in C that checks if singly linked list has a cycle in it
 *
 * @list: linked list parsed into the program
 *
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (!list)
	{
		return (0);
	}

	while (a && b && b->next)
	{
		a = a->next;
		b = b->next->next;

		if (a == b)
		{
			return (1);
		}
	}
	return (0);
}
