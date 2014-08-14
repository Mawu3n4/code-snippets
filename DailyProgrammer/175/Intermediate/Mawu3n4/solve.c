/*
** solve.c for 175 Intermediate in DailyProgrammer/175/Intermediate/Mawu3n4
**
** Made by zackaria dibe
** Contact <contact@zackdibe.com>
**
** Started on  Thu Aug 14 13:56:39 2014 zackaria dibe
** Last update Thu Aug 14 17:29:43 2014 zackaria dibe
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

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

char    *append(char *array, char c) {
  char  *ret = (char *) malloc(sizeof(array) + 2);

  strcpy(ret,array);
  ret[len(ret)] = c;
  ret[sizeof(ret)] = '\0';
  free(array);
  return ret;
}

// Who needs snprintf ?
char    *concat(int n_strings, ...) {
  va_list ap;
  char  *ret, *tmp;
  int   ret_size = 0;

  ret = (char *) malloc(ret_size);
  va_start(ap, n_strings);
  while (n_strings--) {
    tmp = va_arg(ap, char *);
    ret_size += sizeof(tmp);
    ret = (char *) realloc(ret, ret_size);
    strcat(ret, tmp);
  }
  va_end(ap);
  return (ret);
}

// Who needs qsort ?
char    *quickSort(char *data) {
  if (len(data) <= 1)
    return data;
  char pivot = data[0];
  char *left = (char *) malloc(sizeof(data));
  char *right = (char *) malloc(sizeof(data));
  char *equal = (char *) malloc(sizeof(data));

  for (int i = 0; data[i]; ++i) {
    if (data[i] < pivot)
      left = append(left, data[i]);
    else if (data[i] > pivot)
      right = append(right, data[i]);
    else
      equal = append(equal, data[i]);
  }
  return (concat(3, quickSort(left), equal, quickSort(right)));
}

// Who needs strtok ?
void    split(char *str, char **list, char token) {
  int   k = -1;

  while (*str) {
    if (*str != token)
      list[++k] = (char *) malloc(WORD_SIZE);
    for (int j = 0; *str && *str != token; ++j, *str++) {
      list[k][j] = *str;
      list[k][j+1] = '\0';
    }
    if (*str == token) *str++;
  }
  list[++k] = NULL;
}

int     main(int ac, char **av) {
  char  **words;
  char  *letters;

  if (ac != 3)
    return (0);

  words = (char **) malloc(countWords(av[1], ' ') * sizeof(char *));
  letters = (char *) malloc(sizeof(av[2]));
  removeChar(' ', av[2], letters);
  letters = quickSort(letters);
  split(av[1], words, ' ');
}
