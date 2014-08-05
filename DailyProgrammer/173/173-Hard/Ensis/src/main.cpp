#include	<SFML/System.hpp>
#include	<SFML/Graphics.hpp>
#include	<cstdio>
#include	<ctime>
#include	<cstdlib>
#include	<cmath>
#include	"Map.hh"
#include	"Player.hh"

void			drawMap(sf::RenderWindow &rw, Map &m)
{
  sf::Vector2u		sz = rw.getSize();
  sf::Vector2u		node(sz.x / m.getSize(), sz.x / m.getSize());
  sf::CircleShape	c(node.x / 4);
  sf::RectangleShape	line;
  Town			**towns = m.getTowns();

  c.setOrigin(c.getRadius(), c.getRadius());
  c.setFillColor(sf::Color(0, 0, 0));
  line.setFillColor(sf::Color(0, 0, 0));
  for (int y = 0; y < m.getSize(); y++)
    {
      for (int x = 0; x < m.getSize(); x++)
	{
	  std::list<Town *>	&roads = towns[y][x].getRoads();
	  sf::Vector2f		beg((.5 + towns[y][x].getX()) * node.x, (.5 + towns[y][x].getY()) * node.y);
	  c.setPosition(beg.x, beg.y);
	  if (roads.size())
	    rw.draw(c);
	  for (std::list<Town *>::iterator it = roads.begin(); it != roads.end(); it++)
	    {
	      sf::Vector2f	end((.5 + (*it)->getX()) * node.x, (.5 + (*it)->getY()) * node.y);
	      line.setSize(sf::Vector2f(sqrt(pow(beg.y - end.y, 2) + pow(beg.x - end.x, 2)), node.x / 8));
	      line.setRotation(atan2(end.y - beg.y, end.x - beg.x) / (M_PI / 180.0));
	      line.setPosition(beg);
	      rw.draw(line);
	    }
	}
    }
}

void			drawInterface(sf::RenderWindow &rw)
{
  sf::Vector2u		winsz = rw.getSize();
  sf::RectangleShape	rect(sf::Vector2f(winsz.x, winsz.y - winsz.x));

  rect.setPosition(0, winsz.x);
  rect.setFillColor(sf::Color::Black);
  rw.draw(rect);
}

int			main()
{
  sf::RenderWindow	rw(sf::VideoMode(600, 900, 32), "173-Hard", sf::Style::Close);
  sf::Event		event;
  Map			m(10);

  srand(time(NULL));
  rw.setFramerateLimit(40.0);
  while (rw.isOpen())
    {
      while (rw.pollEvent(event))
	{
	  if (event.type == sf::Event::Closed ||
	      (event.type == sf::Event::KeyPressed && event.key.code == sf::Keyboard::Escape))
	    rw.close();
	}
      rw.clear(sf::Color(255, 255, 255));
      drawMap(rw, m);
      drawInterface(rw);
      rw.display();
    }

  return (0);
}
