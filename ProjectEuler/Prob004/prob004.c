
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
