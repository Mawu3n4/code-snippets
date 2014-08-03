#include	"Map.hh"

Map::Map(uint8_t size)
  : _size(size)
{
  _towns = new Town*[_size];
  for (int y = 0; y < _size; y++)
    {
      _towns[y] = new Town[_size];
      for (int x = 0; x < _size; x++)
	_towns[y][x] = Town(x, y);
    }
}

Map::~Map()
{
}

void			Map::_buildRoad(Town &a, Town &b)
{
  a.linkTo(b);
  b.linkTo(a);
}
