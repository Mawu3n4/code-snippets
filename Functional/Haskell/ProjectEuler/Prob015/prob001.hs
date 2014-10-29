
fact x = product [1..x]
solve n m = (fact (n + m)) `quot` ((fact m) * (fact n))