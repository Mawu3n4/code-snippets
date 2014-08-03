#include	<SFML/System.hpp>
#include	<SFML/Graphics.hpp>
#include	<cstdio>
#include	"Map.hh"

void			drawMap(sf::RenderWindow &rw, Map &m)
{
  sf::Vector2u		sz = rw.getSize();
  sf::Vector2u		node(sz.x / m.getSize(), sz.x / m.getSize());
  sf::CircleShape	c(node.x / 4);
  Town			**towns;

  c.setOrigin(c.getRadius(), c.getRadius());
  c.setFillColor(sf::Color(0, 0, 0));
  for (int y = 0; y < m.getSize(); y++)
    {
      for (int x = 0; x < m.getSize(); x++)
	{
	  c.setPosition((.5 + x) * node.x, (.5 + y) * node.y);
	  rw.draw(c);
	}
    }
}

int			main()
{
  sf::RenderWindow	rw(sf::VideoMode(600, 600, 32), "173-Hard", sf::Style::Close);
  sf::Event		event;
  Map			m(10);

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
      rw.display();
    }

  return (0);
}
