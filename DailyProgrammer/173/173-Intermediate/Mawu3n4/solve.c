/*
** solve.c for 173 intermediate in DailyProgrammer/173-Intermediate/Mawu3n4
**
** Made by zackaria dibe
** Contact <contact@zackdibe.com>
**
** Started on  Thu Jul 31 11:58:39 2014 zackaria dibe
** Last update Thu Jul 31 16:11:59 2014 zackaria dibe
*/

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <string.h>

#define WIDTH   50
#define HEIGHT  WIDTH
#define CHUNK   2048
#define ISSPACE(c) (c == '\n')
#define COLOR_SIZE 14

/* To be changed to real colors instead of ASCII char */
int     colorpool[] = {33, 34, 35, 36,
                       37, 38, 39, 40, 41,
                       42, 43, 44, 45, 46};

/* Circular LL used for the nodes of the board */
typedef struct s_node {
  int color;
  int dir;
  struct s_node* next;
} ll_node;

/* Map containing needed informations about the and and the nodes */
typedef struct s_map {
  ll_node **nodes;
  int x_ant;
  int y_ant;
  int dir;
} t_map;

/* Read a line on fd until a SPACE char then returns a copy of it */
char    *readLine(int fd) {
  char  *dest;
  char  *input = NULL;
  size_t  len = 0;
  ssize_t ret;

  ret = getline(&input, &len, fdopen(fd, "r"));
  if (input[ret - 1] == '\n')
    input[ret - 1] = '\0';
  dest = malloc((ret - 1) * sizeof(char));
  dest = strcpy(dest, input);
  free(input);

  return (dest);
}

/* Set the color palet according to the user input */
ll_node *getColors() {
  ll_node *colors = malloc(sizeof(ll_node));;
  /* Keep the root of the circular LL */
  ll_node *head = colors;
  int ret, i = 0;
  char c;

  ret = read(0, &c, 1);
  if (ret && !ISSPACE(c)) {
      colors->color = colorpool[i];
      colors->dir = c == 'R' ? 1 : -1;
  }
  while ((ret = read(0, &c, 1)) && !ISSPACE(c)) {
    ll_node     *tmp = malloc(sizeof(ll_node));

    if (c != 'R' && c != 'L') {
      printf("Error: Unknown direction: [%c]\n", c);
      return (NULL);
    }
    colors->next = tmp;
    i++;
    tmp->color = colorpool[i % COLOR_SIZE];
    tmp->dir = c == 'R' ? 1 : -1;
    colors = tmp;
  }
  colors->next = head;
  return (head);
}

/* Move the ant a step forward */
void    moveAnt(t_map *map) {
  /* Get real pos within the nodes */
  int   pos = map->y_ant * HEIGHT + map->x_ant;

  /* 0 North, 1 Est, 2 South, 3 West */
  int   dir = (4 + dir + map->nodes[pos]->dir) % 4;

  /* Clever and ugly */
  map->y_ant = (HEIGHT + map->y_ant + (-1 + dir) % 2) % HEIGHT;
  map->x_ant = (WIDTH + map->x_ant + (dir & 1) - 2 * (dir == 3)) % WIDTH;

  map->nodes[pos] = map->nodes[pos]->next;
}

void    printMap(ll_node **nodes) {
  int   i;

  for (i = 0; nodes[i]; ++i) {
    printf("%c", nodes[i]->color);
    if (i && !(i % WIDTH))
      printf("\n");
  }
}

int     main(int ac, char **av) {
  ll_node *head;
  int steps, i;
  t_map map;

  /* Get user input */
  head = getColors();
  if (!head)
    return (0);
  steps = atoi(readLine(0));

  /* Init the map */
  map.nodes = malloc(sizeof(ll_node *) * WIDTH * HEIGHT);
  map.x_ant = WIDTH / 2;
  map.y_ant = HEIGHT / 2;
  map.dir = 0;
  for (i = 0; i < WIDTH * HEIGHT; ++i) {
    map.nodes[i] = head;
  }
  map.nodes[i] = NULL;

  while (steps--)
    moveAnt(&map);

  printMap(map.nodes);
}
