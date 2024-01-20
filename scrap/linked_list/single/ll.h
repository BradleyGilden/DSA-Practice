#ifndef LL_H
#define LL_H

#include <stdio.h>
#include <stdlib.h>

typedef struct list {
    int n;
    struct list *next;
} list_t;

void append(list_t *head, int data);
void lprint(list_t *head);
void push(list_t **head, int data);
int lcount(list_t *head);
void addIndex(list_t **head, int data, int index);

#endif /*LL_H*/
