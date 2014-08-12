#include	"Map.hh"
#include	<cstdlib>

Map::Map(uint8_t size)
  : _size(size)
{
  _towns = new Town*[_size];
  for (int y = 0; y < _size; y++)
    {
      _towns[y] = new Town[_size];
      for (int x = 0; x < _size; x++)
	{
	  float		rx = ((float) (rand() % 2000) / 1000. - 1) * 0.1;
	  float		ry = ((float) (rand() % 2000) / 1000. - 1) * 0.1;

	  _towns[y][x] = Town(x, rx, y, ry);
	}
    }
  do
    {
      for (int y = 0; y < _size; y++)
	for (int x = 0; x < _size; x++)
	  _towns[y][x].clearRoads();
      _buildPath(0, 0, 1);
      _buildPath(_size - 1, _size - 1, 5);
      // _buildPath(rand() % _size, 0, 2);
      // _buildPath(0, rand() % _size, 0);
      _buildPath(rand() % _size, _size - 1, 6);
      _buildPath(_size - 1, rand() % _size, 4);
    }
  while (!_checkPath());
  _towns[0][0].visit();
}

Map::~Map()
{
  for (int y = 0; y < _size; y++)
    delete[] _towns[y];
  delete[] _towns;
}

void		Map::_buildRoad(Town &a, Town &b)
{
  a.linkTo(b);
  b.linkTo(a);
}

bool			Map::_checkPath()
{
  std::list<int>	visited;
  std::list<int>	toVisit;
  int			x;
  int			y;

  toVisit.push_back(0);
  while (toVisit.size())
    {
      x = toVisit.front() % _size;
      y = toVisit.front() / _size;
      if (x == _size - 1 && y == _size - 1)
	return (true);
      visited.push_back(toVisit.front());
      toVisit.pop_front();
      std::list<Town *>	roads = _towns[y][x].getRoads();
      for (std::list<Town *>::iterator it = roads.begin(); it != roads.end(); it++)
	{
	  int	id = (*it)->getBaseY() * _size + (*it)->getBaseX();
	  if (std::find(visited.begin(), visited.end(), id) == visited.end())
	    toVisit.push_back(id);
	}
    }
  return (false);
}

void		Map::_buildPath(int x, int y, int dir)
{
  int		len = -2;
  int		dx, dy, nx, ny;

  while (1)
    {
      if (len != -2)
	dir = (dir + 8 + (rand() % 3) - 1) % 8;
      len = rand() % (_size / 6) + (_size / 6);
      dx = dir < 2 || dir > 6 ? 1 : dir > 2 && dir < 6 ? -1 : 0;
      dy = dir > 0 && dir < 4 ? 1 : dir > 4 ? -1 : 0;
      while (--len >= 0)
	{
	  nx = x + dx;
	  ny = y + dy;
	  if (nx < 0 || ny < 0 || nx >= _size || ny >= _size)
	    return;
	  _buildRoad(_towns[y][x], _towns[ny][nx]);
	  x = nx;
	  y = ny;
	}
    }
}
