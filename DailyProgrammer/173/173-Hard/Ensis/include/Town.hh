#ifndef		__TOWN_HH__
#define		__TOWN_HH__

#include	<list>
#include	<string>

class		Town
{
public:
  Town(int x = 0, float dx = 0, int y = 0, float dy = 0)
    : _name(""), _x(x + dx), _y(y + dy), _bx(x), _by(y), _visited(false)
  {}
  ~Town() {}

public:
  bool			linkTo(Town &other) { _roads.push_back(&other); }
  float			getX() const { return (_x); }
  float			getY() const { return (_y); }
  int			getBaseX() const { return (_bx); }
  int			getBaseY() const { return (_by); }
  bool			wasVisited() const { return (_visited); }
  void			visit() { _visited = true; }
  std::list<Town *>	&getRoads() { return (_roads); }
  void			clearRoads() { _roads.clear(); }

private:
  std::list<Town *>	_roads;
  std::string		_name;
  float			_x;
  float			_y;
  int			_bx;
  int			_by;
  bool			_visited;
};

#endif
