import Data.List

getList :: [[Int]]
getList = [ [x,y] | x <- [0..99], y <- [0..99], x < y ]

printElem :: Int -> String
printElem x = if x < 10
                 then "0"++(show x)
                 else (show x)


printList xxs = intercalate " " (map printElem xxs)

solve = putStrLn (intercalate ", " (map printList getList))
