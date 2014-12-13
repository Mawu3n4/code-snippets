#include	<stdarg.h>
#include	<unistd.h>
#include	<stdlib.h>
#include	<string.h>
#include	"raise.h"
#include	"new.h"

void		*new(Class *class, ...)
{
  va_list	ap;
  void		*ret;

  if (!class)
    raise("Invalid instance of Class * ('NULL')");
  if (!(ret = malloc(class->__size__)))
    raise("Out of memory");
  va_start(ap, class);
  memcpy(ret, class, class->__size__);
  if (class->__init__)
    class->__init__(ret, &ap);
  va_end(ap);
  return (ret);
}

void		*va_new(Class *class, va_list *ap)
{
  void		*ret;

  if (!class)
    raise("Invalid instance of Class * ('NULL')");
  if (!(ret = malloc(class->__size__)))
    raise("Out of memory");
  memcpy(ret, class, class->__size__);
  if (class->__init__)
    class->__init__(ret, ap);
  va_end(*ap);
  return (ret);
}

void		delete(Object *ptr)
{
  if (!ptr)
    raise("Invalid instance of Object * ('NULL')");
  if (((Class *) ptr)->__del__)
    ((Class *) ptr)->__del__(ptr);
  free(ptr);
}
