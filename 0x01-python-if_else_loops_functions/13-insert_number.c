#include "lists.h"

/**
 * insert_node - Entry Point
 *
 * @head: the list passed in
 * @number: value of the new node
 *
 * Description: Inserts a node in an ordered linked list
 *
 * Return:  The address of the new node or NULL if failure
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *first;

first = *head;
new = malloc(sizeof(listint_t));

if (new == NULL)
return (NULL);
new->n = number;

if (*head == NULL || (*head)->n > number)
{
new->next = *head;
*head = new;
return (new);
}

while (first->next != NULL)
{
if ((first->next)->n >= number)
{
new->next = first->next;
first->next = new;
return (new);
}
first = first->next;
}
first->next = new;
new->next = NULL;
return (new);
}
