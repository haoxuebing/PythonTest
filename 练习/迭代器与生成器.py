

list = [1, 2, 3, 4, 5]

it = iter(list)  # 创建迭代器
# print(next(it)) #输出迭代器的下一个元素
# print(next(it))
# print(list)

for x in list:
    print(x, end=' ')

for y in it:
    print(y, end=' ')

import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

print()
f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
