fibo :: [Int]
fibo = 1:2:[ x + y | (x, y) <- zip fibo (tail fibo) ]

solve n = sum [ x | x <- takeWhile (< n) fibo, even x]