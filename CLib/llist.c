#include <stdlib.h>

#include "utils.h"
#include "llist.h"

void cll_insert(Node *start, char data) {
  Node *tmp = start;

  while (tmp && tmp->next != start)
    tmp = tmp->next;
  tmp->next = (Node *) malloc(sizeof(Node));
  tmp->next->prev = tmp;
  tmp = tmp->next;
  tmp->data = data;
  tmp->next = start;
}

void ll_insert(Node *start, char data) {
  Node *tmp = start;

  while (tmp && tmp->next)
    tmp = tmp->next;
  tmp->next = (Node *) malloc(sizeof(Node));
  tmp = tmp->next;
  tmp->data = data;
  tmp->next = 0;
}

void ll_print(Node *start) {
  Node *tmp = start;

  while ((tmp = tmp->next) && tmp != start)
    print_char(tmp->data);
  print_char('\n');
}

int ll_isLoop(Node *start) {
  Node *hare, *tort1, *tort2;

  hare = tort1 = tort2 = start;
  while (hare && (tort1 = tort2->next) && (tort2 = tort1->next)) {
    if (hare == tort1 || hare == tort2)
      return (1);
    hare = hare->next;
  }
  return (0);
}

Node* ll_find(Node *start, char to_find) {
  Node *tmp = start;

  while ((tmp = tmp->next) && tmp != start)
    if (tmp->data == to_find)
      return tmp;
  return NULL;
}

int ll_test() {
  Node *llist = (Node *) malloc(sizeof(Node));

  llist->data = 0;
  llist->next = 0;
  print_str("Inserting 'h' in the list\n");
  ll_insert(llist, 'h');
  print_str("Inserting 'e' in the list\n");
  ll_insert(llist, 'e');
  print_str("Inserting 'l' in the list\n");
  ll_insert(llist, 'l');
  print_str("Inserting 'l' in the list\n");
  ll_insert(llist, 'l');
  print_str("Inserting 'o' in the list\n");
  ll_insert(llist, 'o');
  print_str("LList : ");
  ll_print(llist);
  print_str("Is 'l' in the list ?: ");
  print_str(ll_find(llist, 'l') ? "yes\n" : "no\n");
  print_str("Is 'e' in the list ?: ");
  print_str(ll_find(llist, 'e') ? "yes\n" : "no\n");
  print_str("Is 'w' in the list ?: ");
  print_str(ll_find(llist, 'w') ? "yes\n" : "no\n");
  print_str("Is 'L' in the list ?: ");
  print_str(ll_find(llist, 'L') ? "yes\n" : "no\n");
  print_str(ll_isLoop(llist) ? "Circular\n" : "Not circular\n");
  return (1);
}
