#include "btheader.h"

void pre_order(node *root)
{
    if (root == NULL)
        return;

    printf("%d\n", root->data);
    pre_order(root->left);
    pre_order(root->right);
}
