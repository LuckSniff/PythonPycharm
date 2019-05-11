def outer():
    i = 10
    def inner():
        nonlocal  i
        i = i*2
        print(i)
    return inner

ret = outer();
ret()