#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a list
 * @list: a pointer to a list
 * Return: 1 if there is a cycle and 0 otherwise
 */

int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (1)
	listint_t *ptr = list->next;

	while (ptr && ptr != list)
	{
		ptr = ptr->next;
		if (ptr == list)
			return (1);
	}
	return (0);
}
