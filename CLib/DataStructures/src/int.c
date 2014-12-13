#include	<stdlib.h>
#include	<stdarg.h>
#include	<stdio.h>
#include	<string.h>
#include	"raise.h"
#include	"int.h"
#include	"new.h"

typedef struct
{
  Class		base;
  int		n;
}		IntClass;

typedef struct
{
  Class         base;
  int           n;
}               CharClass;

typedef struct
{
  Class         base;
  float         n;
}               FloatClass;

static char const	*Int_str(Object *self)
{
  IntClass	*this = (IntClass *) self;
  char		*str;

  if (!this)
    raise("Invalid instance of IntClass * ('NULL')");
  if (!(str = malloc(strlen(this->base.__name__) + 20 + 6)))
    raise("Out of memory");
  sprintf(str, "<%s (%d)>", this->base.__name__, this->n);
  return (str);
}

static int		get_casted_value(const Object *this)
{
  int			i;

  i = !strcmp(((Class *) this)->__name__, "Int") ? ((IntClass *) this)->n:
      !strcmp(((Class *) this)->__name__, "Int")   ? ((IntClass *) this)->n  :
      !strcmp(((Class *) this)->__name__, "Char")  ? ((CharClass *) this)->n : 0;
  return (i);
}

static Object		*Int_add(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Adds NULL object(s)");
  return (new(Int, get_casted_value(self) + get_casted_value(other)));
}

static Object		*Int_sub(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Substracts NULL object(s)");
  return (new(Int, get_casted_value(self) - get_casted_value(other)));
}

static Object		*Int_mul(const Object *self, const Object *other)

{
  if (!self || !other)
    raise("Multiplies NULL object(s)");
  return (new(Int, get_casted_value(self) * get_casted_value(other)));
}

static Object		*Int_div(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Divides NULL object(s)");
  if (!get_casted_value(other))
    raise("Division by 0");
  return (new(Int, get_casted_value(self) / get_casted_value(other)));
}

static bool		Int_eq(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Compares NULL object(s)");
  return (get_casted_value(self) == get_casted_value(other));
}

static bool		Int_gt(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Compares NULL object(s)");
  return (get_casted_value(self) > get_casted_value(other));
}

static bool		Int_lt(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Compares NULL object(s)");
  return (get_casted_value(self) < get_casted_value(other));
}

static void	Int_ctor(Object* self, va_list *ap)
{
  IntClass	*this = (IntClass *) self;

  if (!this)
    raise("Invalid instance of IntClass * ('NULL')");
  this->n = va_arg(*ap, int);
  this->base.__str__ = &Int_str;
  this->base.__add__ = &Int_add;
  this->base.__sub__ = &Int_sub;
  this->base.__mul__ = &Int_mul;
  this->base.__div__ = &Int_div;
  this->base.__eq__ = &Int_eq;
  this->base.__gt__ = &Int_gt;
  this->base.__lt__ = &Int_lt;
}

static void	Int_dtor(Object* self)
{
  (void) self;
}

static IntClass _description = {
  { sizeof(IntClass), "Int", &Int_ctor, &Int_dtor, &Int_str,
    &Int_add, &Int_sub, &Int_mul, &Int_div,
    &Int_eq, &Int_gt, &Int_lt },
    0
};

Class* Int = (Class*) &_description;
