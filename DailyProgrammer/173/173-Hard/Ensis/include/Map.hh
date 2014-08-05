#ifndef		__MAP_HH__
#define		__MAP_HH__

#include	<list>
#include	<vector>
#include	<algorithm>
#include	<stdint.h>
#include	<iostream>
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
  bool		_checkPath();
  void		_buildRoad(Town &a, Town &b);
  void		_buildPath(int x, int y, int dir);

private:
  Town		**_towns;
  uint8_t	_size;
};

#endif
