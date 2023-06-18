#ifndef _MAIN_H_
#define _MAIN_H_
//modules used
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * list - struct for linked list nodes
 * @age: age of person
 * @name: name of person
 * @next: reference to next node in list
 * */
typedef struct list{
    int age;
    char *name;
    struct list *next;
}list_t;

void print_nodes(list_t *head);
int count_nodes(list_t *head);
void free_nodes(list_t *head);
list_t *add_beg(list_t **head, char *name, int age);
list_t *add_end(list_t *head, char *name, int age);
list_t *add_pos(list_t **head, char *name, int age, int pos);
void del_beg(list_t **head);
void del_end(list_t *head);
void del_pos(list_t **head, int pos);
void reverse(list_t **head);
int llen(list_t *head);
void is_cyclic(list_t *head);
#endif /*_MAIN_H_*/
