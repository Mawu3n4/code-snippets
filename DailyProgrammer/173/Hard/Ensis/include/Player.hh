#ifndef		__PLAYER_HH__
#define		__PLAYER_HH__

class		Player
{
public:
  Player()
    : _money(2.0), _tickets(2), _x(0), _y(0)
  {}
  ~Player() {}

public:
  float		getTicketPrice() const { return (1.0); }

  int		getX() const { return (_x); }
  int		getY() const { return (_y); }
  float		getMoney() const { return (_money); }
  int		getTickets() const { return (_tickets); }

  bool		canBuyTicket() const { return (_money >= getTicketPrice()); }
  bool		canUseTicket() const { return (_tickets); }

  void		buyTicket() { canBuyTicket() && (_money -= getTicketPrice(), _tickets++); }
  int		useTicket() { return (_tickets && --_tickets); }
  void		moveTo(int x, int y) { _x = x; _y = y; }
  void		addTicket(int num) { _tickets += num; }
  void		addMoney(float money) { _money += money; }
  void		subMoney(float money) { _money -= _money > money ? money : _money; }

private:
  float		_money;
  int		_tickets;
  int		_x;
  int		_y;
};

#endif
