
# coding: UTF-8
# import sys
# import support
# from fibonacci import fib,fib2

'''support.print_fun('tom')

print(sys.path)

print('当前:',__name__)

fib(1000)'''

'''
# 读取键盘输入
str1=input('please input:')
print('this is your input: ',str1)
'''

'''文件读写    
f = open('readMe.txt', 'r+', encoding='utf-8')
print(f.read())
f.write("\n再加一行")
f.close()
'''

try:
    s1 = int(input('输入一个数字：'))
    print(s1)
except ValueError as Argument:
    print('this is err:', Argument)
