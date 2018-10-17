import cmath
import random
import calendar

'''
num=int(input('input a num'))
num_sqrt=cmath.sqrt(num)
print(num_sqrt,type(num_sqrt))
'''

'''
for x in range(0, 9):
    print(random.randint(0, 9), end=' ')
'''

'''
try:
    float('qwe')
except ValueError as Argument:
    print(Argument)
    pass

print('hello world')
'''

'''
# 写文件
with open('readMe.txt','a+', encoding='utf-8') as out_file:
    out_file.write('\nthis is a new line')

# 读文件
with open('readMe.txt','r+', encoding='utf-8') as in_file:
    print(in_file.read())
'''

print(calendar.month(2018,9))