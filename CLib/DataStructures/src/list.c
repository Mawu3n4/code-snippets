#include	<stdio.h>
#include	<stdlib.h>
#include	<stdarg.h>
#include	<string.h>

#include	"raise.h"
#include	"list.h"
#include	"new.h"

typedef struct
{
  Object	*_data;
  void		*_next;
}		t_list;

typedef struct
{
  Container	base;
  Class		*_type;
  size_t	_size;
  t_list	*_llist;
}		ListClass;

typedef struct {
  Iterator	base;
  ListClass	*_list;
  t_list	*_it;
  size_t	_idx;
}		ListIteratorClass;

void ListIterator_ctor(ListIteratorClass* self, va_list* args)
{
  size_t	i;

  if (!self)
    raise("Invalid instance of ListIteratorClass * ('NULL')");
  self->_list = va_arg(*args, ListClass *);
  self->_idx = va_arg(*args, unsigned int);
  self->_it = self->_list->_llist;
  i = -1;
  while (++i < self->_idx && self->_it)
    self->_it = self->_it->_next;
  self->_idx = i;
}

bool ListIterator_eq(ListIteratorClass* self, ListIteratorClass* other)
{
  if (!self || !other)
    raise("Invalid instance of ListIteratorClass * ('NULL')");
  return (self->_idx == other->_idx);
}

bool ListIterator_gt(ListIteratorClass* self, ListIteratorClass* other)
{
  if (!self || !other)
    raise("Invalid instance of ListIteratorClass * ('NULL')");
  return (self->_idx > other->_idx);
}

bool ListIterator_lt(ListIteratorClass* self, ListIteratorClass* other)
{
  if (!self || !other)
    raise("Invalid instance of ListIteratorClass * ('NULL')");
  return (self->_idx < other->_idx);
}

void ListIterator_incr(ListIteratorClass* self)
{
  if (!self)
    raise("Invalid instance of ListIteratorClass * ('NULL')");
  if (!self->_it)
    return;
  self->_idx++;
  self->_it = self->_it->_next;
}

Object* ListIterator_getval(ListIteratorClass* self)
{
  if (!self)
    raise("Invalid instance of ListIteratorClass * ('NULL')");
  return (self->_it->_data);
}

void ListIterator_setval(ListIteratorClass* self, ...)
{
  va_list	ap;

  if (!self)
    raise("Invalid instance of ListIteratorClass * ('NULL')");
  va_start(ap, self);
  ((Class *) self->_it->_data)->__init__(self->_it->_data, &ap);
}

static ListIteratorClass ListIteratorDescr = {
    {
        {
            sizeof(ListIteratorClass), "ListIterator",
            (ctor_t) &ListIterator_ctor,
            NULL, /* dtor */
            NULL, /* str */
            NULL, NULL, NULL, NULL, /* add, sub, mul, div */
            (binary_comparator_t) &ListIterator_eq,
            (binary_comparator_t) &ListIterator_gt,
            (binary_comparator_t) &ListIterator_lt,
        },
        (incr_t) &ListIterator_incr,
        (getval_t) &ListIterator_getval,
        (setval_t) &ListIterator_setval,
    },
    NULL,
    NULL,
    0
};

static Class* ListIterator = (Class*) &ListIteratorDescr;

void List_ctor(ListClass* self, va_list* args)
{
  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  self->_size = 0;
  self->_type = va_arg(*args, Class *);
  self->_llist = NULL;
}

void List_dtor(ListClass* self)
{
  t_list	*tmp;

  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  while (self->_llist)
    {
      tmp = tmp->_next;
      free(self->_llist);
      self->_llist = tmp;
    }
}

size_t List_len(ListClass* self)
{
  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  return (self->_size);
}

Iterator* List_begin(ListClass* self)
{
  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  return (new(ListIterator, self, 0));
}

Iterator* List_end(ListClass* self)
{
  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  return (new(ListIterator, self, self->_size));
}

Object* List_getitem(ListClass* self, ...)
{
  ListIteratorClass	*it;
  Object	*obj;
  va_list	ap;
  unsigned int	ix;

  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  va_start(ap, self);
  if ((ix = va_arg(ap, unsigned int)) >= self->_size)
    return (NULL);
  it = new(ListIterator, self, ix);
  obj = ((Container *) it)->__getitem__((Container *) it);
  ((Class *) it)->__del__(it);
  return (obj);
}

void List_setitem(ListClass* self, ...)
{
  ListIteratorClass	*it;
  Object	*obj;
  va_list	ap;
  unsigned int	ix;


  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  va_start(ap, self);
  if ((ix = va_arg(ap, unsigned int)) >= self->_size)
    return;
  it = new(ListIterator, self, ix);
  obj = ((Container *) it)->__getitem__((Container *) it);
  ((Class *) it)->__del__(it);
  ((Class *) obj)->__init__(obj, &ap);
}

void	List_push(ListClass *self, ...)
{
  va_list	ap;
  t_list	*list;

  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  if (!(list = malloc(sizeof(*list))))
    raise("Out of memory");
  va_start(ap, self);
  list->_next = self->_llist;
  list->_data = va_new(self->_type, &ap);
  self->_llist = list;
  self->_size++;
}

void	List_push_back(ListClass *self, ...)
{
  t_list	*it;
  va_list	ap;
  t_list	*list;

  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  if (!(list = malloc(sizeof(*list))))
    raise("Out of memory");
  va_start(ap, self);
  for (it = self->_llist; it && it->_next; it = it->_next);
  if (!it)
    self->_llist = list;
  else
    it->_next = list;
  list->_next = NULL;
  list->_data = va_new(self->_type, &ap);
  self->_size++;
}

Object	*List_pop(ListClass *self)
{
  Object	*obj;
  t_list	*next;

  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  if (!self->_llist)
    return (NULL);
  obj = self->_llist->_data;
  next = self->_llist->_next;
  free(self->_llist);
  self->_llist = next;
  self->_size--;
  return (obj);
}

Object *List_pop_back(ListClass *self)
{
  Object	*obj;
  t_list	*it;

  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  if (!self->_llist)
    return (NULL);
  for (it = self->_llist; it && it->_next && ((t_list *) it->_next)->_next; it = it->_next);
  if (!it->_next)
    {
      self->_llist = NULL;
      obj = self->_llist->_data;
    }
  else
    {
      it->_next = NULL;
      obj = it->_data;
      free(it);
    }
  self->_size--;
  return (obj);
}

Object	*List_front(ListClass *self)
{
  printf("Front\n");
  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  if (!self->_llist)
    return (NULL);
  return (self->_llist->_data);
}

Object *List_back(ListClass *self)
{
  t_list	*it;

  printf("Back\n");
  if (!self)
    raise("Invalid instance of ListClass * ('NULL')");
  if (!self->_llist)
    return (NULL);
  for (it = self->_llist; it && it->_next; it = it->_next);
  return (it->_data);
}

static ListClass _descr = {
    { /* Container */
        { /* Class */
            sizeof(ListClass), "List",
            (ctor_t) &List_ctor, (dtor_t) &List_dtor,
            NULL, /*str */
	    NULL, NULL, NULL, NULL, /* add, sub, mul, div */
            NULL, NULL, NULL, /* eq, gt, lt */
        },
        (len_t) &List_len,
        (iter_t) &List_begin,
        (iter_t) &List_end,
        (getitem_t) &List_getitem,
        (setitem_t) &List_setitem,
	(pop_t) &List_pop,
	(push_t) &List_push,
	(pop_t) &List_pop_back,
	(push_t) &List_push_back,
	(pop_t) &List_front,
	(pop_t) &List_back
    },
    NULL, 0, NULL
};

Class* List = (Class*) &_descr;

