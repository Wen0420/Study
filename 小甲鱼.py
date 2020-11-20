print(5+3)#8
print("5+3")#5+3

print("well water" + "river")
#well waterriver

print("I love u" * 8)

print("I love u\n" * 8)#\n是换行符

print("I love u" + 8)#can only concatenate str (not "int") to str。
print("I love u" + "8")
print("I love u" + str(8))


#P3
print("---工作室---")
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
if guess == 8:
    print("我操，你是小甲鱼心里的蛔虫吗？")
    print("猜中了也没有奖励！")
else:
    print("猜错了，小甲鱼现在心里想的是8！")
print("游戏结束，不玩啦^_^")

#看一下python 有多少个内置函数
dir(__builtins__)

help(input)

#P4
print('let\'s go')

print("let'''s go")

str = 'C:\now'
print(str)

#利用反斜杠对自身进行转义
str = 'C:\\now'
print(str)

str = r'C:\now'
print(str)

str  = '''guaji
guaji
guaji'''
print(str)#打印出来相当于每个guaji后面都加了\n

#p5
print(1>3)

#5.1
print("---工作室---")
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
if guess == 8:
    print("哇操，你是小甲鱼心里的蛔虫吗？")
    print("哼，猜中了也没有奖励！")
else:
    if guess > 8:
        print("哥，大了大了~~")
    else:
        print("嘿，小了！小了！")
print("游戏结束，不玩啦^_^")

#5.2 不想要重复运行程序，想要让程序提供多次机会（即重复运行某些代码）
print("---工作室---")
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
while guess != 8:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == 8:
        print("哇操，你是小甲鱼心里的蛔虫吗？")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > 8:
            print("哥，大了大了~~")
        else:
            print("嘿，小了！小了！")
print("游戏结束，不玩啦^_^")

#5.3 希望程序的答案是随机的
import random
secret = random.randint(1, 10)
print("---工作室---")
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("哇操，你是小甲鱼心里的蛔虫吗？")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~")
        else:
            print("嘿，小了！小了！")
print("游戏结束，不玩啦^_^")

#我自己改了一下
import random
secret = random.randint(1, 10)
print("---工作室---")
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
if guess == secret:
    print("哇操，你是小甲鱼心里的蛔虫吗？")
    print("哼，猜中了也没有奖励！")
while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess > secret:
        print("哥，大了大了~~")
    else:
        print("嘿，小了！小了！")
print("游戏结束，不玩啦^_^")

# ---工作室---
# 不妨猜一下小甲鱼现在心里想的是哪个数字：>? 1
# 游戏结束，不玩啦^_^

5 + 8
print(5 + 8)

#5.2.1 三次不对就结束游戏 homework 动动手 0完善第二个改进要求（为用户提供三次机会尝试，机会用完或者用户猜中答案均退出循环）并改进视频中小甲鱼的代码。
import random

times = 3
secret = random.randint(1, 10)
print('------------------我爱鱼C工作室------------------')
# 这里先给guess赋值（赋一个绝对不等于secret的值）
guess = 0
# print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
# 嗯，小甲鱼觉得富有创意的你应该会尝试用 end="JJ"？
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    guess = int(temp)
    times = times - 1  # 用户每输入一次，可用机会就-1
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
        if times > 0:
            print("再试一次吧：", end=" ")
        else:
            print("机会用光咯T_T")
print("游戏结束，不玩啦^_^")

'''
用guess=0 是赋值。 是为了进入第一个 while 的判断，附一个不可能的值0，因为答案是1-10随机
这样 while中的 guess一定不等于secret, AND times>0,这样，初次就一定可以进入 循环中了。
guess赋值为0，或者赋值为一个不可能的数，为的让while 后的条件同时为真，这样就能进入循环了。
当满足了循环中的条件，就是猜对的时候，这个时候， 就不再满足 guess！=secret，另外的times就不用管了，因为 and 中有一个为FALSE,就都为FALSE，会跳出while，
出现最后的 游戏结束。 游戏结束前还有 上一个循环中的 满足 guess =secret时的结果，猜对了+无奖励。


'''

#1. 尝试写代码实现以下截图功能：homework 004

temp = input('请输入一个整数:')
number = int(temp)
i = 1
while number:
    print(i)
    i = i + 1
    number = number - 1

print(range(10))
#range(0, 10)

#2. 尝试写代码实现以下截图功能：homework 004
temp = input('请输入一个整数:')
number = int(temp)
while number:
    i = number - 1
    while i:
        print(' ', end = '')
        i = i - 1
    j = number
    while j:
        print('*', end = '')
        j = j - 1
    print()
    number = number - 1

 #第二种方法
i = int(input("请输入一个整数："))
while i > 0:
    print(' ' * (i - 1) + '*' * i)
    i = i - 1

#7常用操作符
a = b = c = d = 10
a += 1
b -= 3
c *= 10
d /= 8
print(a) #11
print(b) #7
print(c) #100
print(d) #1.25

print(10//8) #1
print(5%2) #1
print(3**2) #9
print(-3*2 + 5/-2 -4)#-12.5
print(-3**2)#-9
print(3**-2)#0.1111111111111111

#005 homework 动动手 0
import random

times = 3
secret = random.randint(1, 10)

print('------------------我爱鱼C工作室------------------')
guess = 0
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")

while (guess != secret) and (times > 0):
    temp = input()

    if temp.isdigit():
        guess = int(temp)
        if guess == secret:
            print("我草，你是小甲鱼心里的蛔虫吗？！")
            print("哼，猜中了也没有奖励！")
        else:
            if guess > secret:
                print("哥，大了大了~~~")
            else:
                print("嘿，小了，小了~~~")
            if times > 1:
                print("再试一次吧：", end='')
            else:
                print("机会用光咯T_T")
    else:
        print("抱歉，您的输入有误，请输入一个整数：", end='')

    times = times - 1  # 用户每输入一次，可用机会就-1

print("游戏结束，不玩啦^_^")

#005 homework 动动手 1. 写一个程序，判断给定年份是否为闰年。
temp = input('请输入一个年份：')
while not temp.isdigit():
    temp = input("抱歉，您的输入有误，请输入一个整数：")

year = int(temp)
if year/400 == int(year/400):
    print(temp + ' 是闰年！')
else:
    if (year/4 == int(year/4)) and (year/100 != int(year/100)):
        print(temp + ' 是闰年！')
    else:
        print(temp + ' 不是闰年！')

#006 homework 0. 请写一个程序打印出 0~100 所有的奇数。
i = 0
while i <= 100:
    if i % 2 != 0:
        print(i, end=' ')
        i += 1
    else:
        i += 1

#2. 题目：请编程求解该阶梯至少有多少阶？
'''
爱因斯坦曾出过这样一道有趣的数学题：有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。
（小甲鱼温馨提示：步子太大真的容易扯着蛋~~~）

题目：请编程求解该阶梯至少有多少阶？
'''
x = 7
i = 1
flag = 0

while i <= 100:
    if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5):
        flag = 1
    else:
        x = 7 * (i+1) # 根据题意，x一定是7的整数倍，所以每次乘以7
    i += 1

if flag == 1:
    print('阶梯数是：', x)
else:
    print('在程序限定的范围内找不到答案！')
#这里，flag 的作用：判断是否满足条件，退出循环
    #动动手2这样写简单多了
    #第一种
    a = 1
    while not ((a % 3 == 2) and (a % 5 == 4) and (a % 6 == 5) and (a % 7 == 0) and (a % 2 == 1)):
        a += 1
    print(a)
    #动动手2
    #第2种 不确定
# x = 7
# i = 1
# while i<= 100:
#     if (x%2 == 1) and (x%3 == 2 ) and (x%5 == 4) and (x%6 == 5) and (x%7 == 0):
# print('爱因斯坦所求阶梯为;',x)
# x = 7 * (i+1)
# i += 1
# else:
#     x = 7 * (i+1)
#     i += 1
# 循环100次，结果为：
# 爱因斯坦所求阶梯为; 119
# 爱因斯坦所求阶梯为; 329
# 爱因斯坦所求阶梯为; 539

#如果程序为：
# x = 7
# i = 1
# while i<= 100:
#     if (x%2 == 1) and (x%3 == 2 ) and (x%5 == 4) and (x%6 == 5) and (x%7 == 0):
# print('爱因斯坦所求阶梯为;',x)
#     else:
#     x = 7 * (i+1)
#     i += 1

# 结果为：输出无限多个“ 爱因斯坦所求阶梯为; 119 ”
# 原因是：i值被固定为一个大于零的正整数，故而无限循环，解决办法为↓
# print('爱因斯坦所求阶梯为;',x)
# i=0

#
# #9 分支与循环2
#     题目：
#     按照100分制，90分以上成绩为A， 80到90分成绩为B， 60到80成绩为C，60以下为D，
#     写一个程序，当用户输入分数， 自动转换为ABCD的形式打印。
#method 1
score = int(input('请输入一个分数: '))
if 100 >= score >= 90:
    print('A')
if 90 > score >= 80:
    print('B')
if 80 > score >= 60:
    print("C")
if 60 > score >= 0:
    print("D")
if score < 0 or score > 100:
    print("输入错误！")

#method 2
score = int(input("请输入您的分数： "))
if 100 >= score >= 90:
    print('A')
else:
    if 90 > score >= 80:
        print('B')
    else:
        if 80 > score >= 60:
            print("C")
        else:
            if 60 > score >= 0:
                print("D")
            else:
                print("输入错误！")

#method 3
score = int(input("请输入您的分数： "))
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 60:
    print('C')
elif 60 > score >= 0:
    print('D')
else:
    print("输入错误！")

#9      条件表达式（三元操作符）-- 操作符指的就是操作数目
#有了这个三元操作符的表达式，你就可以使用一条语句来完成以下的条件判断和赋值操作：
x, y = 4, 5
if x < y:
    small = x
else:
    small = y
#* 例子可以改进为
small = x if x < y else y

assert 3 > 4

#10
favourite = 'fish'
for i in favourite:
    print(i, end=' ')#end=''是不换行

member = ['小甲鱼', '小布丁', '黑夜', '迷途', '怡静']
#[] 表示列表
for each in member:
    #for 后面是变量的名字，随便用一个就可以了
    print(each, len(member))

member = ['小甲鱼', '小布丁', '黑夜', '迷途', '怡静']
#[] 表示列表
for each in member:
    #for 后面是变量的名字，随便用一个就可以了
    print(each, len(each))

range(5)
#range(0, 5) 返回一个range对象

list(range(5))
#list(BIF)变成一个列表显示出来
#[0, 1, 2, 3, 4] 默认从0开始，但不包括5

for i in range(5):
    print(i)

for i in range(2, 9):
    print(i)
# 2 是包含的，但不包括9

for i in range(1, 10, 2):
    print(i)

#break
#example
bingo = "小甲鱼是帅哥"
answer = input('请输入小甲鱼最想听的一句话：')

while True:
    if answer == bingo:
        break
    answer = input("抱歉，错了，请重新输入（答案正确才能退出游戏）：")

print("哎哟，帅哦~")
print("您真是小甲鱼肚子里的蛔虫啊")
#while 循环它的值是一直为true的，当没有触发到break的时候它是不会跳出循环的

#continue
#例子
for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 2
    print(i)
#i是偶数就+2输出，i是奇数就直接输出。 从0-9每个数对此操作，就会得到。

#homework 第007、008讲：了不起的分支和循环2
#动动手1
#请将以下代码修改为三元操作符实现：

x, y, z = 6, 5, 4
if x < y:
    small = x
    if z < small:
        small = z
elif y < z:
    small = y
else:
    small = z

#我尝试改写后的(不对)
small = x if x < y else y
small = y if y < z else z
#答案：
small = x if (x < y and x < z) else (y if y < z else z)


#007 3
x = 1
y = 2
z = 3
x,y,z = z,y,x
print(z,y,x)

#007 4
name = '小甲鱼'
print('鱼' in name)#true

name = '小甲鱼'
print('肥鱼' in name)#False

#试着改动一下用while
name = 'Turtle'
guess = input('Guess what his name is?')
while True:
    if guess == name:

        break
    guess = input('Then you guess wrong')
print('awesome')

#007 home work 动动手0
#0. 视频中小甲鱼使用 if elif else 在大多数情况下效率要比全部使用 if 要高，但根据一般的统计规律，一个班的成绩一般服从正态分布，也就是说平均成绩一般集中在 70~80 分之间，因此根据统计规律，我们还可以改进下程序以提高效率。

score = int(input('请输入一个分数：'))
if 80 > score >= 60:
    print('C')
elif 90 > score >= 80:
    print('B')
elif 60 > score >= 0:
    print('D')
elif 100 >= score >= 90:
    print('A')
else:
    print('输入错误！')

#homework 第009讲：了不起的分支和循环3
#0
for i in range(0, 10, 2):
    print('I Love FishC')

#1
for i in 5:
    print('I Love FishC')
#'int' object is not iterable

#4
print(range(10))#range(0, 10)
for i in range(10):
    print(i)

for i in range(10):
    print(i, end=' ')

#7. 【学会提高代码的效率】你的觉得以下代码效率方面怎样？有没有办法可以大幅度改进(仍然使用while)？

i = 0
string = 'ILoveFishC.com'
while i < len(string):
    print(i)
    i += 1
#答案
i = 0
string = 'ILoveFishC.com'
length = len(string)
while i < length:
    print(i)
    i += 1

#009 homework 动动手
# 0. 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。
#
# 程序演示如图：
#请输入密码：*****
#密码中不能含有“*”！您还有3次机会！请输入密码：I Love***
#密码中不能含有“*”！您还有3次机会！请输入密码：*** I Love you
#密码中不能含有“*”！您还有3次机会！请输入密码：小甲鱼是帅哥
#密码输入错误！您还有2次机会！请输入密码：呃。。。鱼c好棒！！
#密码输入错误！您还有1次机会！请输入密码：FishC.com
#密码正确，进入程序。。。。。。
#
#try
passport = input('请输入密码')
        #不确定了
    #答案
count = 3
password = 'FishC.com'

while count:
    passwd = input('请输入密码：')
    if passwd == password:
        print('密码正确，进入程序......')
        break
    elif '*' in passwd:
        print('密码中不能含有"*"号！您还有', count, '次机会！', end=' ')
        continue
    else:
        print('密码输入错误！您还有', count-1, '次机会！', end=' ')
    count -= 1

# 1. 编写一个程序，求 100~999 之间的所有水仙花数。
## 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。
#别人写的
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            if a*100+b*10+c == a**3 + b**3 + c**3:
                sun = a*100 + b*10 + c
print(sun)#407
#别人帮忙改进的
num = 100
while 100 <= num < 1000:
    if num == (num % 10) ** 3 + (num // 100) ** 3 + ((num // 10) % 10) ** 3:
        print(num)
    num += 1

#答案
for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10         # 注意这里要使用地板除哦~
    if sum == i:
        print(i)
#
# 2. 三色球问题
#
#
# 有红、黄、蓝三种颜色的球，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。
print('red\tyellow\tgreen')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                # 注意，下边不是字符串拼接，因此不用“+”哦~
                print(red, '\t', yellow, '\t', green)

#注释：range(2, 7) 是产生 [2, 3, 4, 5, 6] 这 5 个数，绿球不能是 1 个，因为如果绿球是 1 个的话，红球 + 黄球需要有 7 个才能符合题意，而红球和黄球每种只有 3 个，因此是 range(2, 7)


#P11
member = ['小甲鱼', '小布丁', '黑夜', '迷途', '怡静']
member.append('福禄娃娃')
print(member)
print(len(member))

member.append('竹林小溪', 'Crazy迷恋')
#TypeError: append() takes exactly one argument (2 given)

member.extend('竹林小溪', 'Crazy迷恋')
#TypeError: append() takes exactly one argument (2 given)

member = ['小甲鱼', '小布丁', '黑夜', '迷途', '怡静']
member.extend(['竹林小溪', 'Crazy迷恋'])
print(member)

member = ['小甲鱼', '小布丁', '黑夜', '迷途', '怡静']
member.insert(1, '牡丹')
print(member)

member = ['小甲鱼', '小布丁', '黑夜', '迷途', '怡静']
member.insert(0, '牡丹')
print(member)

#p12 数组2 列表的其它常用方法
member = ['小甲鱼', '小布丁', '黑夜', '迷途', '怡静', '竹林小溪', 'Crazy迷恋']
print(member[0])

    #如何交换 牡丹和小甲鱼的位置？
        #利用一个中间值，一个零时变量temp 把两者做个交换，首先把小甲鱼这个字符串给了temp这个变量
            #再把牡丹赋值到小甲鱼这个位置
member = ['小甲鱼', '牡丹', '小布丁', '黑夜', '迷途', '怡静', '竹林小溪', 'Crazy迷恋']
temp = member[0]
member[0] = member[1]
print(member)#['牡丹', '牡丹', '小布丁', '黑夜', '迷途', '怡静', '竹林小溪', 'Crazy迷恋']
    #此时小甲在temp里面
member[1] = temp
print(member)#['牡丹', '小甲鱼', '小布丁', '黑夜', '迷途', '怡静', '竹林小溪', 'Crazy迷恋']

member = ['牡丹', '小甲鱼', '小布丁', '黑夜', '迷途', '怡静', '竹林小溪', 'Crazy迷恋']
member.remove('怡静')
print(member)#['牡丹', '小甲鱼', '小布丁', '黑夜', '迷途', '竹林小溪', 'Crazy迷恋']
member.remove('小鱼儿')#ValueError: list.remove(x): x not in list

member = ['牡丹', '小甲鱼', '小布丁', '黑夜', '迷途', '竹林小溪', 'Crazy迷恋']
del member[1]
print(member)

del member #可以删除整个列表

member = ['牡丹', '小甲鱼', '小布丁', '黑夜', '迷途', '竹林小溪', 'Crazy迷恋']
print(member.pop())#Crazy迷恋
print(member)#['牡丹', '小甲鱼', '小布丁', '黑夜', '迷途', '竹林小溪']
print(member.pop(1))#小甲鱼
print(member)#['牡丹', '小布丁', '黑夜', '迷途', '竹林小溪']

member = ['牡丹', '黑夜', '迷途', '竹林小溪']
#分片
print(member[1:3])#['黑夜', '迷途']
#不写0，默认从0开始
print(member[:3])#['牡丹', '黑夜', '迷途']
print(member[1:])#['黑夜', '迷途', '竹林小溪']
print(member[:])#什么都不写得到列表的拷贝 #['牡丹', '黑夜', '迷途', '竹林小溪']

#有的情况想对列表进行修改，但又不想更改原来的列表，就利用：，复制一个列表
member2 = member[:]
print(member2)#['牡丹', '黑夜', '迷途', '竹林小溪']



##P13 数组3 列表的常用操作符
list1 = [123]
list2 = [234]
print(list1 > list2)#False

    #有多个元素的时候，默认从第0个元素开始比较
list1 = [123, 456]
list2 = [234, 123]
print(list1 > list2)#False

    #逻辑判断
list3 = [123, 456]
print((list1 < list2) and (list1 == list3))#True

    #连接
list4 = list1 + list2
print(list4)#[123, 456, 234, 123]
#相当于extend 扩展列表 用list.extend()会更为规范， 因为+不能添加新元素， 例如数字+字符串就不行

list3 = [123, 456]
print(list3*3)#[123, 456, 123, 456, 123, 456]

list3 *= 3
print(list3)

list3 *= 5
print(list3)#这里的list3*=5 为什么是15次，？ 因为list3已经变为含有3次的了，再乘以5变成15次。

print(123 in list3)#True

print('小甲鱼' not in list3)#True

list5 = [123, ['小甲鱼', '牡丹'], 456]
print('小甲鱼' in list5)#False '小甲鱼'是在list 的list里
print('小甲鱼' in list5[1])#True
print(list5[1][0])#牡丹 #外面列表里1的值，里面列表里1的值，

print(dir(list))

print(list3.count(123)) #15

#list.index 会返回参数所在的位置，
print(list3.index(123))#0 只显示了第0 位的。
print(list3.index(123,3,7))# index(参数，参数起始位置，参数结束位置) #4 同样也只显示在这个范围里第一次出现的位置

list3.reverse()
print(list3)#[456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123, 456, 123]

list6 = [4,2,5,1,9,23,32,0]
list6.sort()
print(list6)#[0, 1, 2, 4, 5, 9, 23, 32]
#那么从2到小排列呢？
list6.reverse()
print(list6)#[32, 23, 9, 5, 4, 2, 1, 0]
#太麻烦换一种

list6 = [4,2,5,1,9,23,32,0]
list6.sort(reverse=1)
print(list6)#[32, 23, 9, 5, 4, 2, 1, 0]

#使用分片可以创建list的一个拷贝
list7 = list6[:]
print(list7)#[32, 23, 9, 5, 4, 2, 1, 0]
list8 = list6
print(list8)#[32, 23, 9, 5, 4, 2, 1, 0]
list6.sort()
print(list6)#[0, 1, 2, 4, 5, 9, 23, 32]
print(list7)#[32, 23, 9, 5, 4, 2, 1, 0]
print(list8)#[0, 1, 2, 4, 5, 9, 23, 32]
#list8属于浅拷贝，没有开辟新的内存空空间，他们一个是赋值，一个是引用
#list8 = list6 实际上只是添加一个新的标签指向list6
#list7 = list6[:] 是实实在在的对list6 进行了一个拷贝
















