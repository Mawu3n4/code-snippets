import Data.List

pack' = Data.List.group

pack [] = []
pack (x:xs) = let (first, rest) = span (== x) xs
              in (x:first):pack rest
