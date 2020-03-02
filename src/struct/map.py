a = {'name': '张三', 'sex': '男'}
print(a)
# get
print(a['name'])

# set
a['age'] = 20
print(a)

# delete attribute
del a['name']
print(a)

# set attr with var
b = 'class'
a[b] = 'map'
print(a)

# len
print(len(a))

# str
print(str(a))

# get keys
print(list(a.keys()))

# get items
print(list(a.items()))

# for in
for name in a:
    print(name)
    print(a[name])

# check attr
for 'class' not in a:
    print('class not in a')
else:
    print('class in a')
