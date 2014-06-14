
myLast xxs = getLast xxs
  where
    getLast (x:xs)
      | null xs = x
      | otherwise = getLast xs


-- Solution

-- myLast :: [a] -> a
-- myLast [x] = x
-- myLast (_:xs) = myLast xs