def generateWaHaHa(totalNum):
    for i in range(totalNum):
        yield 'WaHaHa%s'%i

ret = generateWaHaHa(10)
for i in ret:
    print(i)

