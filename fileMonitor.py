def tail(filePath):
    file = open(filePath,encoding='utf-8')
    while True:
        lineContent = file.readline()
        if lineContent.strip():
            yield lineContent.strip()

fileGenerator = tail('file')
for i in fileGenerator:
    if 'python' in i:
        print('** '+i)

