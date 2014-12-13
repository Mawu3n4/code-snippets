
#ifndef CONTAINER_H
# define CONTAINER_H

# include "object.h"
# include "iterator.h"

typedef struct Container_s Container;

typedef Iterator* (*iter_t)(Container* self);
typedef size_t (*len_t)(Container* self);
typedef Object* (*getitem_t)(Container* self, ...);
typedef void (*setitem_t)(Container* self, ...);
typedef void (*push_t)(Container* self, ...);
typedef Object *(*pop_t)(Container* self);

struct Container_s {
  Class base;
  len_t       __len__;
  iter_t      __begin__;
  iter_t      __end__;
  getitem_t   __getitem__;
  setitem_t   __setitem__;
  pop_t	      __pop__;
  push_t      __push__;
  pop_t	      __pop_back__;
  push_t      __push_back__;
  pop_t	      __front__;
  pop_t	      __back__;
};

# define len(c)                 (((Container*) c)->__len__(c))
# define begin(c)               (((Container*) c)->__begin__(c))
# define end(c)                 (((Container*) c)->__end__(c))
# define getitem(c, ...)        (((Container*) c)->__getitem__(c, __VA_ARGS__))
# define setitem(c, ...)        (((Container*) c)->__setitem__(c, __VA_ARGS__))
# define pop(c)			(((Container*) c)->__pop__(c))
# define push(c, ...)		(((Container*) c)->__push__(c, __VA_ARGS__))
# define pop_back(c)		(((Container*) c)->__pop_back__(c))
# define push_back(c, ...)	(((Container*) c)->__push_back__(c, __VA_ARGS__))
# define back(c)		(((Container*) c)->__back__(c))
# define front(c)		(((Container*) c)->__front__(c))

#endif

