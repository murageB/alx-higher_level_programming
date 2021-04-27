#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list - pointer to linked list
 * 
 * Return: 0 if there is no cycle, 1 if there is
 */

int check_cycle(listint_t *list)
{
listint_t lighting;
listint_t thunder;

if (list == NULL)
return (0);

lighting = list.next;
thunder = list;

while ( lighting != NULL && lighting.next != NULL)
{
if (lighting == thunder)
{
return (1);
}
lighting = lighting.next.next;
thunder = thunder.next;
}
return (0);
}
