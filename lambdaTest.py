# divide = lambda x,y : x/y
# add = lambda  x,y : x+y
# max = lambda  x,y : x if x > y else y
# min = lambda  x,y : x if x < y else y
#
# ret = divide(4,2)
# print(ret)
#
# ret = add(1,2)
# print(ret)
#
# ret = max(4,2)
# print(ret)
#
# ret = min(4,2)
# print(ret)


dic={'k1':10,'k2':100,'k3':30}
def fun(key):
    return dic[key]
ret = max(dic,key=fun)
print(ret)

'''
max的排序是根据key指定方法的返回值
一般，max根据传入的参数类型，使用默认的key方法
'''
ret = max(dic,key=lambda x : dic[x])
print(ret)

ret = map(lambda x : x**2 ,[1,2,3,4])
for i in ret:
    print(i)

ret = filter(lambda x : x>10,[1,2,3,11,4])
for i in ret:
    print(i)

'''现有两元祖(('a'),('b')),(('c'),('d')) ， 转变为[{'a':'c'},{'b','d'}]'''
data = zip((('a'),('b')),(('c'),('d')))
ret = map(lambda x:{x[0]:x[1]},data)    #它内部使用的是迭代器
print(list(ret))                        #可迭代数据类型的转换

ret = list(map(lambda x:{x[0]:x[1]},zip((('a'),('b')),(('c'),('d')))) )
print(ret)


def get():
    return [lambda x,i=i : x*i for i in range(4)]
print([m(2) for m in get()])