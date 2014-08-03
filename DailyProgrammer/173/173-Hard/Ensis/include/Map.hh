#ifndef		__MAP_HH__
#define		__MAP_HH__

#include	<vector>
#include	<stdint.h>
#include	<cstdio>
#include	"Town.hh"

class		Map
{
public:
  Map(uint8_t size);
  ~Map();

public:
  uint8_t	getSize() const { return (_size); }
  Town		**getTowns() { return (_towns); }

private:
  void		_buildRoad(Town &a, Town &b);

private:
  Town		**_towns;
  uint8_t	_size;
};

#endif
