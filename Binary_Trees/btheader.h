#ifndef BTHEADER_H
#define BTHEADER_H


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


#endif /*BTHEADER_H*/
