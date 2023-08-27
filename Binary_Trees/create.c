#include "btheader.h"

/**
 * create - creates a binary tree
 * Return: address of new node
 */

node *create(void)
{
    int x;
    node *new = malloc(sizeof(node));
    if (new == NULL)
        return (NULL);
    printf("Enter data (0 for no node):");
    scanf("%d", &x);
    if (x == -1)
        return (NULL);
    new->data = x;
    printf("Enter left child of %d", x);
    new->left = create();
    printf("Enter right child of %d", x);
    new->right = create();
    return (new);
}
