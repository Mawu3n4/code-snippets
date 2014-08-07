#ifndef		__INTERFACE_HH__
#define		__INTERFACE_HH__

#include	<SFML/System.hpp>
#include	<SFML/Graphics.hpp>
#include	<cwchar>
#include	<cstdio>
#include	<ctime>
#include	<cstdlib>
#include	<cmath>
#include	<cstring>
#include	"Map.hh"
#include	"Player.hh"

class		Interface
{
public:
  Interface(sf::RenderWindow &rw, Map &map, Player &player);
  ~Interface();

public:
  void		draw();
  void		drawMap();
  void		drawInterface();

public:
  sf::Vector2f	getBtnSize() const { return (sf::Vector2f(100, 50)); }
  sf::Vector2f	getBtnPosition() const { return (sf::Vector2f(465, 830)); }
  void		setString(const std::string s) { strcpy(_text, s.c_str()); }
  void		setText(char *s) { strcpy(_text, s); }

private:
  sf::RenderWindow	&_rw;
  Map			&_map;
  Player		&_player;
  sf::Texture		_ticketTex;
  sf::Texture		_moneyTex;
  sf::Font		_font;
  char			_text[128];
};

#endif
