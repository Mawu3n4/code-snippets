#include <unistd.h>

#define CHAR(x) (x + '0')

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
