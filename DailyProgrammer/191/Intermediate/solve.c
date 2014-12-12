#include <unistd.h>
#include <stdlib.h>

#include "llist.h"

int main(int ac, char **av) {
  print_str("Testing : ");
  print_str(ll_test() ? "OK" : "FAIL");
  print_str("\n");
}
