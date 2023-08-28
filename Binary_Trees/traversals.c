#include "btheader.h"

void pre_order(node *root)
{
    if (root == NULL)
        return;

    printf("%d ", root->data);
    pre_order(root->left);
    pre_order(root->right);
}

void in_order(node *root)
{
    if (root == NULL)
        return;

    pre_order(root->left);
    printf("%d ", root->data);
    pre_order(root->right);
}

void post_order(node *root)
{
    if (root == NULL)
        return;

    pre_order(root->left);
    pre_order(root->right);
    printf("%d ", root->data);
}
