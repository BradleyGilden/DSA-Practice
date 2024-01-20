#include "ll.h"

int main(void) {
    list_t *head = NULL;

    push(&head, 5);
    push(&head, 6);
    push(&head, 7);
    push(&head, 8);

    append(head, 6);
    append(head, 7);
    append(head, 8);

    addIndex(&head, 100, 7);


    lprint(head);
    return (0);
}
