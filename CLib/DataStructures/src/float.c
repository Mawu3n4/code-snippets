#include	<stdlib.h>
#include	<stdarg.h>
#include	<stdio.h>
#include	<string.h>
#include	"raise.h"
#include	"object.h"
#include	"float.h"
#include	"char.h"
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
  Class		base;
  float		n;
}		FloatClass;

static char const	*Float_str(Object *self)
{
  FloatClass	*this = (FloatClass *) self;
  char		*str;

  if (!this)
    raise("Invalid instance of FloatClass * ('NULL')");
  if (!(str = malloc(strlen(this->base.__name__) + 50 + 6)))
    raise("Out of memory");
  sprintf(str, "<%s (%f)>", this->base.__name__, this->n);
  return (str);
}

static float			get_casted_value(const Object *this)
{
  float			f;

  f = !strcmp(((Class *) this)->__name__, "Float") ? ((FloatClass *) this)->n:
       !strcmp(((Class *) this)->__name__, "Int")   ? ((IntClass *) this)->n  :
       !strcmp(((Class *) this)->__name__, "Char")  ? ((CharClass *) this)->n : 0;
  return (f);
}

static Object		*Float_add(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Adds NULL object(s)");
  return (new(Float, get_casted_value(self) + get_casted_value(other)));
}

static Object		*Float_sub(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Substracts NULL object(s)");
  return (new(Float, get_casted_value(self) - get_casted_value(other)));
}

static Object		*Float_mul(const Object *self, const Object *other)

{
  if (!self || !other)
    raise("Multiplies NULL object(s)");
  return (new(Float, get_casted_value(self) * get_casted_value(other)));
}

static Object		*Float_div(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Divides NULL object(s)");
  if (!get_casted_value(other))
    raise("Division by 0");
  return (new(Float, get_casted_value(self) / get_casted_value(other)));
}

static bool		Float_eq(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Compares NULL object(s)");
  return (get_casted_value(self) == get_casted_value(other));
}

static bool		Float_gt(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Compares NULL object(s)");
  return (get_casted_value(self) > get_casted_value(other));
}

static bool		Float_lt(const Object *self, const Object *other)
{
  if (!self || !other)
    raise("Compares NULL object(s)");
  return (get_casted_value(self) < get_casted_value(other));
}

static void	Float_ctor(Object* self, va_list *ap)
{
  FloatClass	*this = (FloatClass *) self;

  if (!this)
    raise("Invalid instance of FloatClass * ('NULL')");
  this->n = va_arg(*ap, double);
  this->base.__str__ = &Float_str;
  this->base.__add__ = &Float_add;
  this->base.__sub__ = &Float_sub;
  this->base.__mul__ = &Float_mul;
  this->base.__div__ = &Float_div;
  this->base.__eq__ = &Float_eq;
  this->base.__gt__ = &Float_gt;
  this->base.__lt__ = &Float_lt;
}

static void	Float_dtor(Object* self)
{
  (void) self;
}

static FloatClass _description = {
  { sizeof(FloatClass), "Float", &Float_ctor, &Float_dtor, &Float_str,
    &Float_add, &Float_sub, &Float_mul, &Float_div,
    &Float_eq, &Float_gt, &Float_lt },
    0.0f
};

Class* Float = (Class*) &_description;
