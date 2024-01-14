#include "ll.h"

int main(void) {
    list_t *head = NULL;

    addBeginning(&head, 5);
    addBeginning(&head, 6);
    addBeginning(&head, 7);
    addBeginning(&head, 8);

    addEnd(head, 6);
    addEnd(head, 7);
    addEnd(head, 8);

    addIndex(&head, 100, 7);


    lprint(head);
    return (0);
}
