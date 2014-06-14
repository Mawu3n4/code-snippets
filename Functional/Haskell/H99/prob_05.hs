
myReverse xxs = myReverse_acc xxs []
  where
    myReverse_acc [] xxs = xxs
    myReverse_acc (x:xs) xxs = myReverse_acc xs (x:xxs)


-- Solution

-- reverse :: [a] -> [a]
-- reverse [] = []
-- reverse (x:xs) = reverse xs ++ [x]