#include	<stdlib.h>
#include	<stdarg.h>
#include	<stdio.h>
#include	<string.h>
#include	"raise.h"
#include	"char.h"
#include	"float.h"
#include	"object.h"
#include	"int.h"
#include	"new.h"

typedef struct
{
  Class         base;
  int           n;
}               IntClass;

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

static char const	*Char_str(Object *self)
{
  CharClass	*this = (CharClass *) self;
  char		*str;

  if (!this)
    raise("Invalid instance of CharClass * ('NULL')");
  if (!(str = malloc(strlen(this->base.__name__) + 20 + 6)))
    raise("Out of memory");
  sprintf(str, "<%s (%d)>", this->base.__name__, this->n);
  return (str);
}

static char		get_casted_value(const Object *this)
{
  char				c;

  c = !strcmp(((Class *) this)->__name__, "Float") ? ((FloatClass *) this)->n:
       !strcmp(((Class *) this)->__name__, "Int")   ? ((IntClass *) this)->n  :
       !strcmp(((Class *) this)->__name__, "Char")  ? ((CharClass *) this)->n : 0;
  return (c);
}

static Object		*Char_add(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Adds NULL object(s)");
  return (new(Char, get_casted_value(self) + get_casted_value(other)));
}

static Object		*Char_sub(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Substracts NULL object(s)");
  return (new(Char, get_casted_value(self) - get_casted_value(other)));
}

static Object		*Char_mul(const Object *self, const Object *other)

{
  if (!self || !other)
    raise("Multiplies NULL object(s)");
  return (new(Char, get_casted_value(self) * get_casted_value(other)));
}

static Object		*Char_div(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Divides NULL object(s)");
  if (!get_casted_value(other))
    raise("Division by 0");
  return (new(Char, get_casted_value(self) / get_casted_value(other)));
}

static bool		Char_eq(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Compares NULL object(s)");
  return (get_casted_value(self) == get_casted_value(other));
}

static bool		Char_gt(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Compares NULL object(s)");
  return (get_casted_value(self) > get_casted_value(other));
}

static bool		Char_lt(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Compares NULL object(s)");
  return (get_casted_value(self) < get_casted_value(other));
}

static void	Char_ctor(Object* self, va_list *ap)
{
  CharClass	*this = (CharClass *) self;

  if (!this)
    raise("Invalid instance of CharClass * ('NULL')");
  this->n = va_arg(*ap, int);
  this->base.__str__ = &Char_str;
  this->base.__add__ = &Char_add;
  this->base.__sub__ = &Char_sub;
  this->base.__mul__ = &Char_mul;
  this->base.__div__ = &Char_div;
  this->base.__eq__ = &Char_eq;
  this->base.__gt__ = &Char_gt;
  this->base.__lt__ = &Char_lt;
}

static void	Char_dtor(Object* self)
{
  (void) self;
}

static CharClass _description = {
  { sizeof(CharClass), "Char", &Char_ctor, &Char_dtor, &Char_str,
    &Char_add, &Char_sub, &Char_mul, &Char_div,
    &Char_eq, &Char_gt, &Char_lt },
    0
};

Class* Char = (Class*) &_description;
