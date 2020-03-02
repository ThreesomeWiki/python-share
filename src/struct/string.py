a = 'hello'
b = "hello"
c = '''
    hello
    world
    '''
print(a, b, c)
# add
print(a + b)
print(f"{a} {b}")

# slice
print(a[0])
print(a[0:1])
print(a[1:])
print(a[-2:])

# length
print(len(a))

# find
# return 0
print(a.find('h'))
# return 1
print(a.find('y'))

# index
# return 0
print(a.index('h'))
