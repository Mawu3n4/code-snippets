
myButLast :: [a] -> a
myButLast (x:[xs]) = x
myButLast (_:xs) = myButLast xs


-- Solution

-- myButLast :: [a] -> a
-- myButLast = last . init