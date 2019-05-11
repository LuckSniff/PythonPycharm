def readSegmentalFile(filePath,everyReadLen):
    file = open(filePath,encoding='utf-8')
    while True:
        content = file.read(everyReadLen)
        if content:
            yield content
'''
g = readSegmentalFile('file',10)
for i in g:
    print('** ' + i)


def generator():
    print('a')
    yield 1
    print('b')
    yield

g = generator()
ret = g.__next__()
print(ret)
ret = g.__next__()
print(ret)

def generateWaHaHa(totalNum):
    for i in range(totalNum):
        yield 'WaHaHa%s'%i

for i in generateWaHaHa(3):
    print(i)
 '''

callable()

