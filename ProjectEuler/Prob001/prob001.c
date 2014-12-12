
#include "utils.h"

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
