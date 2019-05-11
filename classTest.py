class A:
    def __init__(self,*args):
        self.name = args[0]
    def __call__(self, *args, **kwargs):
        print('调用call')

class Foo:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __getitem__(self, item):
        return self.__dict__[item]
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __delitem__(self, key):
        print('del %s'%self.__dict__[key])
        del self.__dict__[key]
    def __delattr__(self, item):        #对应的是 del f.age方法


f = Foo('Li',14,'男')
print(f['name'])
f['age'] = 15
print(f['age'])
print(f.__dict__)
del f.__dict__['age']
print(f.__dict__)



