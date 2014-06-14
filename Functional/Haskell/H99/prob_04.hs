
myLength' [] n = n
myLength' (_:xs) n = myLength' xs (n + 1)
myLength xxs = myLength' xxs 0


-- Solution

-- myLength           :: [a] -> Int
-- myLength []        =  0
-- myLength (_:xs)    =  1 + myLength xs