#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse - reverse
 * @head: pointer to list to be reversed
 * Return: void
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev, *current, *next, *h;

	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	h = prev;
	return (h);
}
/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: pointer to head of list
 * Return: 1 if it is Palindrome , 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	if (!(*head))
		return (1);

	listint_t *aux, *current, *currentR, *h;

	h = *head;
	current = *head;
	aux = reverse(&current);
	currentR = aux;
	reverse(&aux);

	while (current != NULL)
	{
		if (current->n == currentR->n)
			current = current->next;
		else
			return (0);
		reverse(&h);
		currentR = currentR->next;
		reverse(&aux);
	}
	return (1);
}
