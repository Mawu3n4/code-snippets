
myReverse xxs = myReverse_acc xxs []
  where
    myReverse_acc [] xxs = xxs
    myReverse_acc (x:xs) xxs = myReverse_acc xs (x:xxs)

isPalindrome xxs = xxs == (myReverse xxs)


-- Solution

-- isPalindrome :: (Eq a) => [a] -> Bool
-- isPalindrome xs = xs == (reverse xs)
-- isPalindrome' []  = True
-- isPalindrome' [_] = True
-- isPalindrome' xs  = (head xs) == (last xs) && (isPalindrome' $ init $ tail xs)isPalindrome :: (Eq a) => [a] -> Bool
