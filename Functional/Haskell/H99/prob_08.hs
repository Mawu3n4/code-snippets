
import Data.List

compress :: Eq a => [a] -> [a]          -- Explicit typing found on SO
compress = map head . Data.List.group


-- Solution

-- Got it ! Yay