#ifndef		__ROAD_HH__
#define		__ROAD_HH__

#include	"Town.hh"

class		Road
{
public:
  Road(Town &a, Town &b);
  ~Road();

private:
  Town		&_a;
  Town		&_b;
};

#endif
