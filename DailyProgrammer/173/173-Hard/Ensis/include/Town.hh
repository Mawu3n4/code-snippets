#ifndef		__TOWN_HH__
#define		__TOWN_HH__

#include	<list>
#include	<string>

class		Town
{
public:
  Town(float x = 0, float y = 0);
  ~Town();

public:
  bool			linkTo(Town &other) { _roads.push_back(&other); }

private:
  std::list<Town *>	_roads;
  std::string		_name;
  float			_x;
  float			_y;
};

#endif
