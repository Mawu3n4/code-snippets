#include	"Interface.hh"

Interface::Interface(sf::RenderWindow &rw, Map &map, Player &player)
  : _rw(rw), _map(map), _player(player)
{
  _ticketTex.loadFromFile("resources/ticket.png");
  _moneyTex.loadFromFile("resources/euro.png");
  _font.loadFromFile("resources/DejaVuSans.ttf");
  _text[0] = '\0';
}

Interface::~Interface()
{
}

void		Interface::draw()
{
  drawMap();
  drawInterface();
}

void		Interface::drawMap()
{
  sf::Vector2u		sz = _rw.getSize();
  sf::Vector2u		node(sz.x / _map.getSize(), sz.x / _map.getSize());
  sf::CircleShape	c(node.x / 4);
  sf::RectangleShape	line;
  Town			**towns = _map.getTowns();

  c.setOrigin(c.getRadius(), c.getRadius());
  c.setFillColor(sf::Color::Black);
  c.setOutlineColor(sf::Color::Red);
  line.setFillColor(sf::Color(0, 0, 0));
  for (int y = 0; y < _map.getSize(); y++)
    {
      for (int x = 0; x < _map.getSize(); x++)
	{
	  bool			goal = (y == _map.getSize() - 1 && x == _map.getSize() - 1);
	  std::list<Town *>	&roads = towns[y][x].getRoads();
	  sf::Vector2f		beg((.5 + towns[y][x].getX()) * node.x, (.5 + towns[y][x].getY()) * node.y);
	  if (towns[y][x].wasVisited() || goal)
	    {
	      c.setPosition(beg.x, beg.y);
	      c.setFillColor(goal ? sf::Color::Blue : sf::Color::Black);
	      c.setOutlineThickness((x == _player.getX() && y == _player.getY()) * 10);
	      _rw.draw(c);
	      for (std::list<Town *>::iterator it = roads.begin(); it != roads.end() && !goal; it++)
		{
		  sf::Vector2f	end((.5 + (*it)->getX()) * node.x, (.5 + (*it)->getY()) * node.y);
		  line.setSize(sf::Vector2f(sqrt(pow(beg.y - end.y, 2) + pow(beg.x - end.x, 2)), node.x / 8));
		  line.setOrigin(0, line.getSize().y / 2);
		  line.setRotation(atan2(end.y - beg.y, end.x - beg.x) / (M_PI / 180.0));
		  line.setPosition(beg);
		  _rw.draw(line);
		}
	    }
	}
    }
}

void		Interface::drawInterface()
{
  sf::Sprite		sprite;
  sf::Text		txt;
  sf::Vector2u		winsz = _rw.getSize();
  sf::RectangleShape	rect(sf::Vector2f(winsz.x, winsz.y - winsz.x));
  sf::Vector2u		msz = _moneyTex.getSize();
  sf::Vector2u		tsz = _ticketTex.getSize();
  wchar_t		buf[8];

  rect.setPosition(0, winsz.x);
  rect.setFillColor(sf::Color::Black);
  _rw.draw(rect);
  rect.setSize(getBtnSize());
  rect.setPosition(getBtnPosition());
  rect.setFillColor(sf::Color::White);
  _rw.draw(rect);

  sprite.setTexture(_ticketTex);
  sprite.setOrigin(tsz.x / 2, tsz.y / 2);
  sprite.setRotation(5);
  sprite.setPosition(300, winsz.y - 40);
  _rw.draw(sprite);
  sprite.setRotation(-15);
  _rw.draw(sprite);

  sprite.setTexture(_moneyTex);
  sprite.setTextureRect(sf::IntRect(0, 0, msz.x, msz.y));
  sprite.setOrigin(msz.x / 2, msz.y / 2);
  sprite.setPosition(50, winsz.y - 40);
  _rw.draw(sprite);

  txt.setFont(_font);
  txt.setOrigin(0, txt.getCharacterSize() / 2);

  swprintf(buf, sizeof(buf) / sizeof(*buf), L"%.1f €", _player.getMoney());
  txt.setString(buf);
  txt.setPosition(100, winsz.y - 40);
  _rw.draw(txt);

  swprintf(buf, sizeof(buf) / sizeof(*buf), L"x%d", _player.getTickets());
  txt.setString(buf);
  txt.setPosition(375, winsz.y - 40);
  _rw.draw(txt);

  txt.setCharacterSize(50);
  txt.setOrigin(0, 0);
  txt.setString(_text);
  txt.setPosition(10, winsz.x + 10);
  _rw.draw(txt);

  txt.setCharacterSize(15);
  txt.setStyle(sf::Text::Bold);
  txt.setColor(sf::Color::Red);
  txt.setOrigin(0, txt.getCharacterSize() / 2);
  txt.setString("Buy a ticket");
  txt.setPosition(winsz.x - 133, winsz.y - 48);
  _rw.draw(txt);
}
