#include "ll.h"
#include <stdio.h>

int llen(list_t *head) {
    int count = 0;

    for (; head; head = head->next)
        count++;
    return count;
}

void addEnd(list_t *head, int data) {
    if (head == NULL)
        return;

    list_t *new = malloc(sizeof(list_t));

    if (new == NULL)
        return;

    new->next = NULL;
    new->n = data;

    while (head->next != NULL) {
        head = head->next;
    }
    head->next = new;
}

void addBeginning(list_t **head, int data) {

    if (head == NULL) {
        return;
    }

    list_t *new = malloc(sizeof(list_t));

    new->next = *head;
    new->n = data;
    *head = new;
}

void addIndex(list_t **head, int data, int index) {

    if (head == NULL)
        return;

    int len = llen(*head);
    list_t *ptr = *head;

    if (index == 0 || *head == NULL) {
        addBeginning(head, data);
        return;
    } else if (index == len) {
        addEnd(*head, data);
        return;
    } else if (index > len) {
        fprintf(stderr, "index out of range");
        exit(1);
    }

    for (int i = 0; i < index - 1; i++) {
        ptr = ptr->next;
    }

    list_t *new = malloc(sizeof(list_t));
    new->n = data;
    new->next = ptr->next;
    ptr->next = new;
}

void lprint(list_t *head) {
    while (head != NULL) {
        printf("%d ", head->n);
        head = head->next;
    }
    printf("\n");
}
