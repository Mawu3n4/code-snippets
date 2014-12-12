#ifndef		LLIST_H_
# define	LLIST_H_

typedef struct node {
  char data;
  struct node *prev;
  struct node *next;
} Node;

#endif		//LLIST_H__

/* Take care of prev and next pointers */
void cll_insert(Node *start, char data);

/* Take care of next pointer, will be NULL for the last node */
void ll_insert(Node *start, char data);

void ll_print(Node *start)
int ll_isLoop(Node *start);
