#include "btheader.h"

/**
 * main - basic implementation of Binary Tree in C
 * Return: 0 Always
 */

int main(void)
{
    // create root
    node *root;
    root = create();
    printf("Pre-order is: ");
    pre_order(root);
}
