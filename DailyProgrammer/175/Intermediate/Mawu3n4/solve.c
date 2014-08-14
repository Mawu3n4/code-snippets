/*
** solve.c for 175 Intermediate in DailyProgrammer/175/Intermediate/Mawu3n4
**
** Made by zackaria dibe
** Contact <contact@zackdibe.com>
**
** Started on  Thu Aug 14 13:56:39 2014 zackaria dibe
** Last update Thu Aug 14 14:22:30 2014 zackaria dibe
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define WORD_SIZE       26

int     len(char *s) {
  return (s[0] ? len(&s[1]) + 1 : 0);
}

int     countWords(char *s, char c) {
  return (s[0] ? (s[0] == c) + countWords(&s[1], c) : 1);
}

void    removeChar(char occ, char *str, char *ret) {
  do
    if (*str != occ)
      *ret++ = *str;
  while (*str++);
}

void    split(char *str, char **list, char token) {
  int   i = 0;

  list[i] = malloc(WORD_SIZE);
  do {
    if (*str != token)
      *(list[i])++ = *str;
    else {
      *(list[i])++ = '\0';
      list[++i] = malloc(WORD_SIZE);
    }
  } while (*str++);

  *(list[i])++ = '\0';
  list[i + 1] = NULL;
}

int     main(int ac, char **av) {
  char  **words;
  char  *letters;

  if (ac != 3)
    return (0);

  words = malloc(countWords(av[1], ' ') * sizeof(char *));
  letters = malloc(len(av[2]));
  removeChar(' ', av[2], letters);
  split(av[1], words, ' ');
  while (*words)
    printf("%s\n", *words++);
}
