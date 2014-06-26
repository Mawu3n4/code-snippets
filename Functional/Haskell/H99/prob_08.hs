
compress xxs = compress' xxs []
  where
    compress' (x:y:xs) compressed
      | x == y = compress' (x:xs) compressed
      | x == [] = compressed
      | otherwise = compress' xs (compressed ++ x)
