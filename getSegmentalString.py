
def getSegmentalString(string,everyLen):
    start = 0
    end = start + everyLen
    part = string[start:end]
    while True:
        yield part
        start = end
        end = start + everyLen
        part = string[start:end]

g = getSegmentalString('abcdef',2)
ret = g.__next__()
print(ret)
