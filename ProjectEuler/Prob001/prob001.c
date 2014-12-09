
#include <unistd.h>

#define CHAR(x) (x + '0')

void print_char(char c) {
  write(1, &c, 1);
}

void print_nb(int nb) {
  if (nb < 10) {
    print_char(CHAR(nb));
  } else {
    print_nb(nb / 10);
    print_nb(nb % 10);
  }
}

int solve(int limit) {
  return (limit
          ? !(limit % 3) || !(limit % 5)
          ? limit + solve(limit - 1) : solve(limit - 1)
          : 0);
}

int main(void) {
  print_nb(solve(1000-1));
  print_char('\n');
  return (0);
}
