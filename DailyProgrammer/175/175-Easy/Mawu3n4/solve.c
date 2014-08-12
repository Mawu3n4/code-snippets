/*
** solve.c for #175 Easy in watch-me-learn/DailyProgrammer/175/175-Easy/Mawu3n4
**
** Made by zackaria dibe
** Contact <contact@zackdibe.com>
**
** Started on  Tue Aug 12 13:24:42 2014 zackaria dibe
** Last update Tue Aug 12 14:21:37 2014 zackaria dibe
*/

/* TODO: Make it as ineficient as possible */

#include <stdlib.h>
#include <stdio.h>

#define SWAP(c1, c2) if (c1 ^ c2) {c1 ^= c2; c2 ^= c1; c1 ^= c2;}

int     len(char *s) {
  return (s[0] ? len(&s[1]) + 1 : 0);
}

void    shuffle(char *s) {
  int   i = len(s);
  int   rand_pos;

  while (--i) {
    rand_pos = rand() % (i + 1);
    SWAP(s[i], s[rand_pos]);
  }
}

int     is_equal(char *s1, char *s2) {
  while (*s1 && *s1++ == *s2++);
  return (*s1++ ? 0 : 1);
}

int     bogo_sort(char *start, char *end) {
  shuffle(start);
  return (is_equal(start, end) ? 0 : 1 + bogo_sort(start, end));
}

int main(int ac, char **av) {
  if (ac < 3) return (0);
  printf("%d iterations\n", len(av[1]) == len(av[2]) ?
         bogo_sort(av[1], av[2]) : 0);
}
