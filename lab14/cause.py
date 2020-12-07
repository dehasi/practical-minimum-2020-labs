e = Exception("Some message", 1, 2)
raise ValueError('failed') from e
