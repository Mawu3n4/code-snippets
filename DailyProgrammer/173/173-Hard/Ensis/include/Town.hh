#ifndef		__TOWN_HH__
#define		__TOWN_HH__

#include	<string>

class		Town
{
public:
  Town(const std::string &name, float x, float y);
  ~Town();

private:
  std::string	_name;
  float		_x;
  float		_y;
};

#endif
