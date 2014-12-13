
#include <stdio.h>
#include <assert.h>

#include "list.h"
#include "int.h"
#include "float.h"
#include "new.h"
#include	"object.h"
#include	"container.h"

void	print_list(Object *list)
{
  Object* it = begin(list);
  Object* it_end = end(list);

  while (lt(it, it_end))
    {
      printf("%s\n", str(getval(it)));
      incr(it);
    }
}

int  main()
{
  Object* list = new(List, Int);
  Object *obj = new(List, Int);;
  Object *test = new(List, Float);
  Object *res;

  push_back(list, 5);
  push_back(list, 42);
  push_back(list, 0);
  push_back(list, -1);
  push_back(list, -84);

  push(obj, 5);
  push(obj, 42);
  push(obj, 0);
  push(obj, -1);
  push(obj, -84);

  print_list(list);
  res = front(list);
  printf("%s\n", str(res));
  res = back(list);
  printf("%s\n\n", str(res));
  print_list(obj);
  return (0);
}

