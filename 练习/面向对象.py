class MyClass:
    def f(self):
        return 'hello world'

x=MyClass()
print(x.f())

#类定义
class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# 实例化类
p = people('runoob',10,30)
p.speak()

class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
       print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade)) 

s=student('ken',10,60,3)
s.speak()
# s.speakTo()
super(student,s).speak()

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class sample(student,speaker):
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

t=sample('Tom',25,80,4,'Python')
t.speak()
