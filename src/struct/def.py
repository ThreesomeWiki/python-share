if 0:
    print('true')

else:
    print('false')

a = 12
while a > 0:
    # can not use a--/a++
    a -= 1
    print(a)

a = 123
# 4508868176
print(id(a))
a += 1
# 4508868208 内存地址更改
print(id(a))


def fun1(name='lisi'):
    print(name)


fun1('张三')
fun1()

# 函数参数


def fun2(func):
    func()


fun2(fun1)


# 函数返回

def fun3(a):
    def fun4(b):
        print(a+b)
    return fun4


fun3(1)(2)
