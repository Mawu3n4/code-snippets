#ifndef		__PLAYER_HH__
#define		__PLAYER_HH__

class		Player
{
public:
  Player()
    : _money(2.0), _tickets(0)
  {}
  ~Player();

public:
  float		getTicketPrice() const { return (1.0); }

  float		getMoney() const { return (_money); }
  int		getTickets() const { return (_tickets); }

  bool		canBuyTicket() const { return (_money > getTicketPrice()); }
  bool		canUseTicket() const { return (_tickets); }

  void		buyTicket() { canBuyTicket() && (_money -= getTicketPrice(), _tickets++); }
  int		useTicket() { return (_tickets && --_tickets); }

private:
  float		_money;
  int		_tickets;
};

#endif
