print('e = Exception()')
e = Exception()
print(e)
print(e.args)
print(e.__cause__)

print('e = Exception("Some message", 1,2,3)')
e = Exception("Some message", 1, 2, 3)
print(e)
print(e.args)
print(e.__cause__)

try:
    raise ValueError('failed') from e
except ValueError as e:
    print('except ValueError as e')
    print(e)
    print(e.args)
    print(e.__cause__)
