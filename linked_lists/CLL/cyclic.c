#include "main.h"

void is_cyclic(list_t *head)
{
    list_t *slow = head;
    list_t *fast = NULL;

    if (head == NULL)
    {
        printf("List is empty\n");
        return;
    }
    fast = slow->next;

    while (fast != NULL)
    {
        if (fast == slow)
        {
            printf("Cycle detected\n");
            return;
        }
        slow = slow->next;
        fast = fast->next;
        if (fast != NULL)
            fast = fast->next;
    }
    printf("No Cycle detected\n");
}
