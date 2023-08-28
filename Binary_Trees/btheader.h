#ifndef BTHEADER_H
#define BTHEADER_H

#include <stdio.h>
#include <stdlib.h>

/**
 * node_s - structure of a Binary Tree node represented by doubly linkable node
 * data: integer data
 * left: pointer to left child
 * right: pointer to right child
 */

typedef struct node_s
{
    int data;
    struct node_s *left, *right;
} node;

node *create(void);
void pre_order(node *root);
void in_order(node *root);
void post_order(node *root);

#endif /*BTHEADER_H*/
