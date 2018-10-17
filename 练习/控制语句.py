'''age = int(input("请输入你家狗狗的年龄: "))
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)
 
### 退出提示
input("点击 enter 键退出")'''



list = [1, 2, 3, 4]
it = iter(list)    # 创建迭代器对象
print(next(it))    # 调用迭代器
for x in it:
    print(x, end=" ")
print('')

for v in range(0,10):
    print(v,end=' ')