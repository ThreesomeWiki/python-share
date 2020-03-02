def time(func):
    print(1)

    def decorator(self):
        func(self)
        print(2)
    return decorator


class A(object):
    def __init__(self, name):
        self.name = name

    @time
    def getName(self):
        print(self.name)


a = A('张三')
a.getName()
