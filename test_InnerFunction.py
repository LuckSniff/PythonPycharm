def isOdd(x):
    return x%2==1

def isString(x):
    return isinstance(x,str)
# or return type(x)==str

testList1 = [1,2,3,4,5,6,7,8]
testList2 = [1,2,3,'hello',5,6,7,8]

# ret = filter(isOdd,testList1)
# for i in ret:
#     print(i)

ret = filter(isString,testList2)
for i in ret:
    print(i)

ret = map(abs,[1,-2,3,5])
for i in ret:
    print(i)

