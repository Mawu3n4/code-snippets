
elementAt [] _ = error "Index out of bounds"
elementAt (x:xs) 1 = x
elementAt (_:xs) pos = elementAt xs (pos - 1)


-- Solution

-- elementAt :: [a] -> Int -> a
-- elementAt list i    = list !! (i-1)