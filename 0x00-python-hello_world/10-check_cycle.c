#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list - pointer to linked list
 * 
 * Return: 0 if there is no cycle, 1 if there is
 */

int check_cycle(listint_t *list)
{
listint_t *lighting = list->next;
listint_t *thunder = list;

if (list == NULL)
return (0);

while ( lighting != NULL && lighting->next != NULL)
{
lighting = (lighting->next)->next;
thunder = thunder->next;

if (lighting == thunder)
return (1);
}
return (0);
}
