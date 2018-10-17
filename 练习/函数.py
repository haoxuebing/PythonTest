
def hello():
    print('hello world')


hello()

# 计算面积


def area(width, height):
    return width*height


w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


# strings, tuples, 和 numbers 是不可更改的对象
def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)  # 结果是 2

# list,dict,set 等则是可以修改的对象


def changeme(mylist):
    mylist.extend([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)

# 修改set


def changeSet(myset):
    myset.add('abcd')


lset = set(('abc', 'qwe'))
print(lset)
changeSet(lset)
print(lset)


# 不定参数
def printinfo(arg1, *vartuple):
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)

# 修改作用域
abc = 'hello'
def test():
    global abc
    abc = abc+'c'
    print(abc)
test()
print(abc)
