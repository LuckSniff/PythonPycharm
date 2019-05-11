'''
egg_list = ['egg%s' %i for i in range(10) ]
print(egg_list)

egg_list = [ i for i in range(10) ]
print(egg_list)

egg_list = [ i*2 for i in range(10) ]
print(egg_list)


g = (i for i in range(10))
for i in g:
    print(i)
'''

'''30内所有能被3整除的数
tmp = [i for i in range(30) if i%3==0]
print(tmp)
names = '1'
ret = [ name for list in names for name in list if name.count('e')==2]
print(ret)
'''

'''合并大小写对应的value值，将k统一成小写'''
value = {'A':'hello','B':'test','c':'good','a':'post','b':'best'}
tmp = {k.lower(): (value.get(k.lower(),'')+value.get(k.upper(),''))for k in value.keys()}
print(tmp)


'''集合推导式'''
tmp = {x**2 for x in [1,-1,2]}
print(tmp)
