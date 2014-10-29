primes = 2 : filter ((==1) . length . primeFactors) [3,5..]

primeFactors n = factor n primes
    where
      factor n (x:xs)
          | x*x > n         = [n]
          | n `mod` x == 0  = x : factor (n `div` x) (x:xs)
          | otherwise       = factor n xs

solve n = last (primeFactors n)
