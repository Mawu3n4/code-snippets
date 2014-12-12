
#include <unistd.h>

#include "utils.h"

int isPalindrome(int n) {
  int reversed = 0, tmp = n;

  while (n > 0) {
    reversed *= 10;
    reversed += n % 10;
    n /= 10;
  }

  return (reversed == tmp);
}


int solve() {
  int i = 99, j = 99;
  int largest = 0, res = 0;

  while (++i < 1000) {
    j = i;
    while (++j < 1000) {
      res = i*j;
      largest = isPalindrome(res) && res > largest ? res : largest;
    }
  }

  return (largest);
}

int main(void) {
  print_nb(solve());
  print_char('\n');
  return (0);
}
