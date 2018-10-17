'''
str = "this is programe 加点中文"
# 首字母大写
print("str.capitalize() : ", str.capitalize())
# 填充成40个字符串
print(str.center(40, '*'))
# count() 方法用于统计字符串里某个字符出现的次数
print(str.count('i'))
'''

''' 编码 解码
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
'''
# 以xx结尾
#print(str.endswith('加点中文', 0))

'''
list1 = ['a', 'c', 'd']
print(list1)
list2 = ['e', 'f']
list1.extend(list1)
print(list1)
'''

# 字典
'''
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("dict['Alice']: ", dict['Name'])
str1 = '菜鸟教程'
print(str1)
'''

'''
dict = {'Name': 'Runoob', 'Age': 7}
for i, j in dict.items():
    print(i, ":\t", j)

for item in dict:
    print(item,'\t',dict[item])
'''

'''
#列表
arr1 = ['a', 'b', 3, 'c']
print(type(arr1), arr1)
#元组
tup1 = ('e', 'r', 77, 'g')
print(type(tup1), tup1)
#字典
dir1 = {'Name': 'Tom', 'Age': 24}
print(type(dir1),dir1)
#集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(type(basket), basket)
'''

'''
a = set('qwerasdf')
print(type(a), a)

b=set()
b.add('abc')
print(type(b),b)

a.update(b)
print(a)
'''
