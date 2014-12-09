
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

int fibo(int n) {
  return (!n ? 0 : n == 1 ? 1 : fibo(n - 1) + fibo(n - 2));
}

int solve(int limit) {
  int sum = 0;
  int fib_i = 1;
  int fib_j = 2;

  while (fib_j < limit) {
    sum += fib_j % 2 ? 0 : fib_j;
    fib_j += fib_i;
    fib_i = fib_j - fib_i;
  }
  return sum;
}

int main(void) {
  print_nb(solve(4000000));
  print_char('\n');
  return (0);
}
