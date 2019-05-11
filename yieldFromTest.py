def generator():
    a = 'abcde'
    yield from a

g = generator()
ret = g.__next__()
print(ret)