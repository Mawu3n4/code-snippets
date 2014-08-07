#include	<SFML/System.hpp>
#include	<SFML/Graphics.hpp>
#include	<iostream>
#include	<cstdio>
#include	<ctime>
#include	<cstdlib>
#include	<cmath>
#include	"Map.hh"
#include	"Player.hh"
#include	"Interface.hh"

void		genEvent(Interface &i, Player &p)
{
  char		buf[128];
  std::string	fmt[5];
  float		money = 0;
  int		r = rand() % (sizeof(fmt) / sizeof(*fmt));

  fmt[0] = "You begged for money\nand got %.2f euros !";
  fmt[1] = "You played some neat\nmusic and received\n%.2f euros !";
  fmt[2] = "Some asshole stole\n%.2f euros in your\npocket...";
  fmt[3] = "A tourist just gave\nyou 2 tickets !";
  fmt[4] = "You found a clean\nticket on the ground !";

  switch (r)
    {
    case 0:
      money = (rand() % 100) / 100.0 + 0.25;
      p.addMoney(money);
      break;
    case 1:
      money = (rand() % 200) / 100.0 + 0.50;
      p.addMoney(money);
      break;
    case 2:
      money = (rand() % 50) / 100.0;
      p.subMoney(money);
      break;
    case 3:
      p.addTicket(2);
      break;
    case 4:
      p.addTicket(1);
      break;
    }
  sprintf(buf, fmt[r].c_str(), money);
  i.setText(buf);
}

int			main()
{
  srand(time(NULL));

  sf::RenderWindow	rw(sf::VideoMode(600, 900, 32), "173-Hard", sf::Style::Close);
  sf::Event		event;
  Map			m(10);
  Player		p;
  Interface		interface(rw, m, p);

  interface.setString("Homeless... Starving...\nNo choice left...\nGo get the meatballs !");
  rw.setFramerateLimit(40.0);
  while (rw.isOpen())
    {
      while (rw.pollEvent(event))
	{
	  if (event.type == sf::Event::Closed ||
	      (event.type == sf::Event::KeyPressed && event.key.code == sf::Keyboard::Escape))
	    rw.close();
	  if (event.type == sf::Event::MouseButtonPressed)
	    {
	      if (event.mouseButton.button == sf::Mouse::Left)
		{
		  if (p.getX() == m.getSize() - 1 && p.getY() == m.getSize() - 1)
		    continue;
		  if (event.mouseButton.y < rw.getSize().x)
		    {
		      int		sz = rw.getSize().x / m.getSize();
		      sf::Vector2u	node(event.mouseButton.x / sz, event.mouseButton.y / sz);
		      Town		&t = m.getTowns()[node.y][node.x];
		      int		dx = event.mouseButton.x - (.5 + t.getX()) * sz;
		      int		dy = event.mouseButton.y - (.5 + t.getY()) * sz;

		      if (dx * dx + dy * dy < sz * sz / 16)
			{
			  std::list<Town *>	&roads = m.getTowns()[p.getY()][p.getX()].getRoads();
			  for (std::list<Town *>::iterator it = roads.begin(); it != roads.end(); it++)
			    {
			      if (node.x == (*it)->getBaseX() && node.y == (*it)->getBaseY())
				{
				  if (p.canUseTicket())
				    {
				      p.useTicket();
				      p.moveTo(node.x, node.y);
				      t.visit();
				      if (node.x == m.getSize() - 1 && node.y == m.getSize() - 1)
					interface.setString("You managed to make\nit to the meatballs !\nEnjoy :)");
				      else
					genEvent(interface, p);
				    }
				  else
				    interface.setString("You don't have any\ntickets... Buy more or\nretry !");
				  break;
				}
			    }
			}
		    }
		  else
		    {
		      sf::Vector2f	sz = interface.getBtnSize();
		      sf::Vector2f	pos = interface.getBtnPosition();
		      sf::Vector2f	mouse(event.mouseButton.x, event.mouseButton.y);

		      if (mouse.x >= pos.x && mouse.y >= pos.y &&
			  mouse.x < pos.x + sz.x && mouse.y < pos.y + sz.y)
			{
			  if (p.canBuyTicket())
			    {
			      p.buyTicket();
			      interface.setString("You bought a ticket...");
			    }
			  else
			    interface.setString("You need money if you\nwant to buy a ticket !");
			}
		    }
		}
	    }
	}
      rw.clear(sf::Color(255, 255, 255));
      interface.draw();
      rw.display();
    }
  return (0);
}
