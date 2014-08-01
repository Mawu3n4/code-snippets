#include	<cstdio>
#include	<cstdlib>
#include	<cstring>
#include	<stdint.h>

class		Sim
{
public:
  Sim(char **av)
  {
    _moves = av[0];
    _end = atoi(av[1]);
    _it = 0;
    _len = strlen(_moves);
    _height = 256;
    _width = 256;
    _x = _width >> 1;
    _y = _height >> 1;
    _dir = 0;
    _map = new char*[_height];
    for (uint32_t y = 0; y < _height; y++)
      {
	_map[y] = new char[_width];
	for (uint32_t x = 0; x < _width; x++)
	  _map[y][x] = 0;
      }
  }
  ~Sim()
  {
    for (uint32_t i = 0; i < _height; i++)
      delete[] _map[i];
    delete[] _map;
  }

  void		step()
  {
    _dir = (4 + _dir + (_moves[(int) _map[_y][_x]] == 'L' ? -1 : 1)) % 4;
    _map[_y][_x] = (_map[_y][_x] + 1) % _len;
    _x = (_width + _x + ((-_dir + 2) * (_dir % 2))) % _width;
    _y = (_height + _y + ((_dir - 1) * !(_dir % 2))) % _height;
    _it++;
  }

  void		print()
  {
    printf("P6\n%d %d\n255\n", _width, _height);
    for (uint32_t y = 0; y < _height; y++)
      for (uint32_t x = 0; x < _width; x++)
	for (int i = 0; i < 3; i++)
	  putchar((_map[y][x] * 255) / (_len - 1));
  }

  uint32_t	getIteration() { return (_it); }
  uint32_t	getMaxIteration() { return (_end); }

private:
  int		_x;
  int		_y;
  char		_dir;
  uint32_t	_it;
  uint32_t	_end;
  char		*_moves;
  int		_len;
  char		**_map;
  uint32_t	_width;
  uint32_t	_height;
};

int		main(int ac, char **av)
{
  Sim		*sim;

  if (ac < 3)
    {
      printf("Usage: ./langton <colors> <iterations>\n");
      return (1);
    }
  sim = new Sim(av + 1);
  while (sim->getIteration() < sim->getMaxIteration())
    sim->step();
  sim->print();
  delete sim;
  return (0);
}
