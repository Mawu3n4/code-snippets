import Data.List

compress xxs = (map head . group) xxs

-- Solution

-- compress :: Eq a => [a] -> [a]
-- compress = map head . group