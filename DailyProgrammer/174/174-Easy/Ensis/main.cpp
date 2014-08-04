#include	<string>
#include	<iostream>
#include	<algorithm>

int		main(int ac, char **av)
{
  std::string	s = "0";

  ac = ac > 1 ? atoi(av[1]) : 0;
  while (ac-- > 0 && (s += s, 1))
    for_each(s.begin() + s.size() / 2, s.end(), [](char &c){c ^= 1;});
  std::cout << s << std::endl;
  return (0);
}
