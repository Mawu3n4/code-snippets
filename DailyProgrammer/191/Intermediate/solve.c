#include <unistd.h>
#include <stdlib.h>

#define CHAR(x) (x + '0')

typedef struct node {
  char data;
  struct node *prev;
  struct node *next;
} Node;

void print_char(char c) {
  write(1, &c, 1);
}

int my_strlen(char *s) {
  return (*s++ ? my_strlen(s) + 1 : 0);
}

void print_str(char *str) {
  if (*str) {
    print_char(*str++);
    if (str)
      print_str(str);
  }
  else
    return;
}


void print_nb(int nb) {
  if (nb < 10) {
    print_char(CHAR(nb));
  } else {
    print_nb(nb / 10);
    print_nb(nb % 10);
  }
}

void ll_insert(Node *start, char data) {
  Node *tmp = start;

  while (tmp && tmp->next != start)
    tmp = tmp->next;
  tmp->next = (Node *) malloc(sizeof(Node));
  tmp->next->prev = tmp;
  tmp = tmp->next;
  tmp->data = data;
  tmp->next = start;
}

void ll_print(Node *start) {
  Node *tmp = start;

  while ((tmp = tmp->next) != start)
    print_char(tmp->data);
  print_char('\n');
}

Node* ll_find(Node *start, char to_find) {
  Node *tmp = start;

  while ((tmp = tmp->next) != start)
    if (tmp->data == to_find)
      return tmp;
  return NULL;
}

int ll_test() {
  Node *llist = (Node *) malloc(sizeof(Node));

  llist->data = 0;
  llist->prev = llist;
  llist->next = llist;
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
  return (1);
}

int main(int ac, char **av) {
  print_str("Testing : ");
  print_str(ll_test() ? "OK" : "FAIL");
  print_str("\n");
}
