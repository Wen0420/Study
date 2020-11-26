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


#homework 010
#动动手0
member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
member.insert(1, 88)
member.insert(3,90)
member.insert(5,85)
member.insert(7,90)
member.append(88)
print(member)



#方法二，复制列表？

#010 1
for item in member:
    print(item)

#010 2 ?
#方法一：
count = 0
length = len(member)
while count < length:
    print(member[count], member[count + 1])
    count += 2

count = 0
length = len(member)
while count < length:
    count += 2
    print(member[count], member[count + 1])
#IndexError: list index out of range

count = 0
length = len(member)
while count < length:
    print(member[count], member[count + 1])
#如果不加打印条件程序就会一直循环打印，小甲鱼，88

member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
print(len(member))#10
print(member[count])#NameError: name 'count' is not defined

count = 0
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
print(len(member))#10
print(member[count])#小甲鱼
print(member[count], member[count + 1])#小甲鱼 88

count += 2
print(member[count], member[count + 1])#迷途 85

count += 1
print(member[count], member[count + 1])#85 怡静


#方法二：重新创建一个同名字的列表覆盖。


#看一下
for each in range(len(member)):
    if each % 2 == 0:
        print(member[each], member[each + 1])

member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
for item in range(len(member)):
    print(item)
#这是竖着打印0123456789

member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
print(member)#['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
for item in member:
    print(member)#打印了十次这个列表#['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

for item in member:
    print(item)#竖着打印了member列表里面的每一项

member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
print(len(member))#
print(range(len(member)))#range(0, 10) 生成以10结束，的数字序列



#练习#2
name = ['F', 'i', 's', 'h']
name.append(['.', 'C'])
print(name)
#['F', 'i', 's', 'h', ['.', 'C']]


name.extend(['.', 'C'])
print(name)
#['F', 'i', 's', 'h', '.', 'C']

#请看以下示例：

name = ['F', 'i', 's', 'h']
name.append('C')
print(name)
name.extend(['.', 'c'])
print(name)
name.append(['.', 'c'])
print(name)


#homework 011
list1 = [1, 3, 2, 9, 7, 8]
print(len(list1))#6, 但如果数位置的话只到第5位
print(list1[0:6])
print(list1[2:5])#[2, 9, 7]
print(list1[0:6:2])#[1, 2, 7]

# 011 1
list1 = [1, 3, 2, 9, 7, 8]
print(list1[0])#1
print(list1[0:1])#[1]
#不一样，list1[0] 返回第0个元素的值，list1[0:1] 返回一个只含有第0个元素的列表。

#2. 如果你每次想从列表的末尾取出一个元素，并将这个元素插入到列表的最前边，你会怎么做？
list1.insert(0, list1.pop())
print(list1)#[8, 1, 3, 2, 9, 7]

#3有些鱼油比较调皮，他说我想试试 list1[-3:-1] 会不会报错，怎么知道一试居然显示 [9, 7]，这是怎么回事呢？
## python 支持负数索引
'''
正常下标 0  1  2  3  4  5
列表内容 1  3  2  9  7  8
负数下标 -6 -5 -4 -3 -2 -1
'''

# 011 4 在进行分片的时候，我们知道分片的开始和结束位置需要进行指定，但其实还有另外一个隐藏的设置：步长。

#1) 之前提到的“简洁”分片操作在这里有效：
list1 = [1, 3, 2, 9, 7, 8]
print(list1[::2])#[1, 2, 7]

print(list1[:6:2])#[1, 2, 7]

##2) 步长不能为0

##3) 步长可以是负数，改变方向（从尾部开始向左走）：

print(list1[::-2])#[8, 9, 3]

#012 1
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
print(list1[1])#[1, 2, ['小甲鱼']]
print(list1[1][2])#['小甲鱼']
print(list1[1][2][0])#小甲鱼

list1[1][2][0] = '小鱿鱼'
print(list1)#[1, [1, 2, ['小鱿鱼']], 3, 5, 8, 13, 18]

#012 5 建立动态列表

list1 = [x ** 2 for x in range(10)]
print(list1)#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#相当于
list1 = []
for x in range(10):
    list1.append(x**2)
    print(list1)
'''
[0]
[0, 1]
[0, 1, 4]
[0, 1, 4, 9]
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25]
[0, 1, 4, 9, 16, 25, 36]
[0, 1, 4, 9, 16, 25, 36, 49]
[0, 1, 4, 9, 16, 25, 36, 49, 64]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
'''
list1 = []
for x in range(10):
    list1.append(x)
    print(list1)
'''
[0]
[0, 1]
[0, 1, 2]
[0, 1, 2, 3]
[0, 1, 2, 3, 4]
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5, 6]
[0, 1, 2, 3, 4, 5, 6, 7]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

for x in range(10):
    print(x)

'''
0
1
2
3
4
5
6
7
8
9
'''

print(range(10))#range(0, 10)

print(len(range(10)))#10

#012. 3 要对一个列表进行逆序排序，请问使用什么方法？
'''''
列表名.sort()
列表名.reverse()

或者

列表名.sort(reverse=True)
'''''

#4. 列表还有两个内置方法没给大家介绍，不过聪明的你应该可以自己摸索使用的门道吧：copy() 和 clear()
 #copy() 方法跟使用切片拷贝是一样的：
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list2 = list1.copy()
print(list2)#[1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]

#clear() 方法用于清空列表的元素，但要注意，清空完后列表仍然还在哦，只是变成一个空列表。
list2.clear()
print(list2)#[]

#5. 问题：请先在 IDLE 中获得下边列表的结果，并按照上方例子把列表推导式还原出来。

list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]
print(list1)
#[(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (2, 1), (2, 3), (2, 5), (2, 7), (2, 9), (4, 1), (4, 3), (4, 5), (4, 7), (4, 9), (6, 1), (6, 3), (6, 5), (6, 7), (6, 9), (8, 1), (8, 3), (8, 5), (8, 7), (8, 9)]



list1 = []
for x in range(10):
    for y in range(10):
        if x%2 == 0:
            if y%2 != 0:
                list1.append((x, y))
print(list1)
#[(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (2, 1), (2, 3), (2, 5), (2, 7), (2, 9), (4, 1), (4, 3), (4, 5), (4, 7), (4, 9), (6, 1), (6, 3), (6, 5), (6, 7), (6, 9), (8, 1), (8, 3), (8, 5), (8, 7), (8, 9)]

list = []
for x in range(10):
    for y in range(10):
        list.append(x,y)
print(list)
#TypeError: append() takes exactly one argument (2 given)

list = []
for x in range(10):
    for y in range(10):
        list.append((x,y))
print(list)
#[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9)]

#6. 活学活用：请使用列表推导式补充被小甲鱼不小心涂掉的部分
list1 = ['1.Just do it', '2.一切皆有可能', '3.让编程改变世界', '4. Impossible is Nothing']
list2 = ['4.阿迪达斯', '2.李宁', '3.鱼C工作室', '1.耐克']
list3 = ['''''']#内容被涂掉了
for each in list3:
    print(each)
#答案
list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]

list1 = ['1.Just do it', '2.一切皆有可能', '3.让编程改变世界', '4. Impossible is Nothing']
list2 = ['4.阿迪达斯', '2.李宁', '3.鱼C工作室', '1.耐克']
list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]
for each in list3:
    print(each)
'''
1.耐克：Just do it
2.李宁：一切皆有可能
3.鱼C工作室：让编程改变世界
4.阿迪达斯： Impossible is Nothing
'''
print(list1[0])#1.Just do it
print(list1[2:])#['3.让编程改变世界', '4. Impossible is Nothing']

#P14 元组：一个不可改变的类型

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple1)#(1, 2, 3, 4, 5, 6, 7, 8)

print(tuple1[5:])#(6, 7, 8)
print(tuple1[:5])#(1, 2, 3, 4, 5)

#也可以用冒号进行元组的切片操作
tuple2 = tuple1[:]
print(tuple2)#(1, 2, 3, 4, 5, 6, 7, 8)

tuple1[1] = 3
#TypeError: 'tuple' object does not support item assignment

#小括号是否就代表元组？
#举个例子
temp = [1]
print(temp)#[1]
type(temp)#<class 'list'>

temp = (1)
print(temp)#1
type(temp)#<class 'int'>

temp2 = 2, 3, 4
type(temp2)#<class 'tuple'>
#所以对于元组来说，是关键 （）不是关键

#想要创建一个空元组
##先看一下空列表
temp = []
type(temp)#<class 'list'>

##创建一个空元组
temp = ()
type(temp)#<class 'tuple'>

#如果要创建的元素只有一个元素，那么要确保它后面有‘，’
##看下例子
temp = (1,)
print(temp)#(1,)
type(temp)#<class 'tuple'>

temp = 1,
print(temp)#(1,)
type(temp)#<class 'tuple'>

print(8 * (8))#64

print(8 * (8,))#(8, 8, 8, 8, 8, 8, 8, 8)

#    更新和删除一个元组
temp = ('小甲鱼', '黑夜', '迷途', '小布丁')
#希望在迷途和小布丁之间插入‘怡静’该怎么写呢？

temp = ('小甲鱼', '黑夜', '迷途', '小布丁')
temp = temp[:2] + ('怡静',) + temp[2:]
print(temp)#('小甲鱼', '黑夜', '怡静', '迷途', '小布丁')
#相当于是元素拆成两部分，再加上一个元组， 把元组贴上一个标签把原来的元组覆盖掉，原来的元组就没有标签了

del temp
print(temp)#NameError: name 'temp' is not defined

##P 15 字符串，各种奇葩的内置方法
str1 = 'I love fishc.com'
print(str1[:6])#I love
print(str1[5])#e
print(str1[:6] + '插入字符串' + str1[6:])#I love插入字符串 fishc.com

str2 = 'xiaoxie'
print(str2.capitalize())#Xiaoxie

str2 = 'XIAOxie'
print(str2.casefold())#xiaoxie
        ##注意每次都是返回一个新的字符串

#swapcase()#大写变小写，小写变大写
str2 = 'XIAOxie'
print(str2.swapcase())#xiaoXIE

#center(width) 居中 自动填充长度
str2 = 'XIAOxie'
print(str2.center(40))#                XIAOxie

#ljust(width) 左对齐
print(str2.ljust(40))#XIAOxie

##lstrip() 去掉字符传中左边所有的空格
str2 = '         XIAOxie'
print(str2.lstrip())#XIAOxie

##rstrip() 去掉字符传中右边（末尾）所有的空格
str2 = '         XIAOxie          '
print(str2.rstrip())#         XIAOxie

#strip() 去除左右空格，但中间空格不去除
str2 = '     a    k    '
print(str2.strip())#a    k
#给定参数
str2 = '    ssss aa aasss  '
print(str2.strip('s'))#    ssss aa aasss

str2 = '    ssssaaaasss  '
print(str2.strip('s'))#    ssssaaaasss


str2 = 'ssssaaaasss'
print(str2.strip('s'))#aaaa


#count(sub[start[,end]]) 返回子字符串在字符串里出现的次数
print(str2.count('xi'))#1

#endswith 检查字符串是否以子字符串结尾
print(str2.endswith('xi'))#False
print(str2.endswith('e'))#True

#expendtabs([tabsize=8]) 把字符串中的tab号（\t）转换为空格，如不指定参数，默认空格tabsize = 8
str3 = 'I\tlove\tFishC.com!'
print(str3.expandtabs())#I       love    FishC.com! 前面一部分包含I有8个空格， 后面一部分包含love有8个空格

str3 = 'I   love    FishC.com!'
print(str3.expandtabs())#I   love    FishC.com!

#find(sub[,start[,end]]) 检查sub是否包含在字符串中，如果有则返回索引值， 否则返回-1
print(str3.find('stf'))#-1
print(str3.find('o'))#5

#rfind(sub[,start[,end]]) 类似于find方法，但它是从右边查找
print(str3.find('stf'))#-1
print(str3.find('o'))#5

#index(sub[,start[,end]]) 和find 方法一样，只不过如果sub 不再string 中会产生异常
print(str3.index('stf'))#ValueError: substring not found
print(str3.index('o'))#5

#islower
str5 = '小甲鱼'
print(str5.islower())#False

#join(sub) 以字符串作为分隔符，插入到sub 中所有的字符之间
str5 = 'Fishc'
print(str5.join(12345))#TypeError: can only join an iterable

str5 = 'Fishc'
print(str5.join('12345'))#1Fishc2Fishc3Fishc4Fishc5

#partition 把字符串 按照参数隔开
str6 = 'I love fishc'
print(str6.partition('ov'))#('I l', 'ov', 'e fishc')

#replace(old,new[,count) 把旧的字符串换成新的字符串， 如果指定了第三个参数则替换不超过这个count次
print(str6.replace('fishc','FishC'))#I love FishC

#split()自动切片操作， 不带参数默认是以空格作为操作符
print(str6.split())#['I', 'love', 'fishc']

print(str6.split('i'))#['I love f', 'shc']

#translate(table)
str7 = 'sssssaaaasssss'#希望把s 转成b
print(str7.translate(str.maketrans('s', 'b')))#bbbbbaaaabbbbb

print(str.maketrans('s', 'b'))#{115: 98} 返回一个字典，中间的数字是：ACSII阿斯特码



#P16 格式化
    #replacement
print("{0} love {1}.{2}".format("I", "FishC", "com"))#I love FishC.com
#format 方法是需要参数的， 这里的0，1，2是位置参数，我们需要给它三个参数

print("{a} love {b}.{c}".format("I", "FishC", "com"))#KeyError: 'a'
#a,b,c是关键字参数
print("{a} love {b}.{c}".format(a="I", b="FishC", c="com"))#I love FishC.com

print("{0} love {b}.{c}".format("I", b="FishC", c="com"))#I love FishC.com
#注意：位置参数必须在关键字参数前

print("{a} love {b}.{0}".format(a="I", b="FishC", ))#SyntaxError: positional argument follows keyword argument

#如何将花括号打印出来呢？
#\t 是打印一个tab 位置
print('\ta')#	a

#打印反斜杠用\\
print('\\')#\

#打印{} 这里的{}相当于把参数转换成字符而不是位置参数
print("{{0}}".format("不打印"))#{0}
#“不打印”是因为没有字段可以被输出的

print('{0:.1f}(1)'.format(27.678, 'GB'))#27.7(1)

print('{0:.1f}{1}'.format(27.678, 'GB'))#27.7GB
#这里格式表示应该是：0.1f,f是定点数和float 是类似的， 也就是只留，一位小数（四舍五入）


#字符串格式化符号含义
# %c 它格式化字符及其ASCII码
print('%c' % 97)#a
#python 接受字典和元组的输入

#如果有多个参数要用元组的方式括起来
print('%c' '%c' '%c' % (97, 98, 99))#abc

# %s 是格式化字符串
print('%s' % 'I love FishC.com')#I love FishC.com

#%d 格式化整数
print('%d + %d = %d' % (4, 5, 4+5))#4 + 5 = 9

print('%d + %d = %d' % (4, 5, 6))#4 + 5 = 6

print('%d + %d = %d' % (4, 5, 9))#4 + 5 = 9

# %o 格式化无符号八进制数
#A0 = 10*16^1 + 0 *16*0 = 160
print('%o' % 10)#12 #这里是把十进制的10转换成了八进制
#八进制转换为十进制公式：2*8^0 + 1* 8^1 = 10

#十六进制是abc 小写x大写X ABC，
print('%x' % 10)#a

print('%X' % 10)#A

print('%X' % 160)#A0

# %f表示格式化定点数，可指定小数点后的精度
print('%f' % 27.658)#27.658000
#浮点数默认精确到六位小数

# %e 使用科学计数法来格式化定点数
print('%e' % 27.658)#2.765800e+01

print('%E' % 27.658)#2.765800E+01

# %g 根据值的大小来决定使用%f或%e
print('%g' % 27.658)#27.658

#格式化操作符辅助指令

# m.n m是显示的最小总宽度（小数点左边的东西），n是小数点后的位数
print('%5.1f' % 27.658)#  27.7
#这里27前面有两个空格指的是，小数点左边的总宽度（即所站的位置数）
print('%5.12f' % 27.658)#  27.658000000000

print('%5.2f' % 27.658)#  27.66

print('%1.2f' % 27.658)#27.66
#小数点左边的数字是打酱油的

print('%.2e' % 27.658)#2.77e+01

# - 用于左对其
print('%-10d' % 5) #5
print('%10d' % 5)#         5

print(len('%10d' % 5))#10

# + 在正数前面显示一个加号
print('%+d' % 5)#+5
print('%+d' % -5)#-5(正号就不显示了)

# # 在八进制前面显示‘0’， 在十六进制数前面显示‘0x’， 或‘0X’
print('%#o' % 10)#0o12 表示它是八进制的意思

print('%#X' % 108)#0X6C 表示它是十进制的意思

print('%#d' % 10)#10 表示它是十六进制的意思

# 0 数字前面用0 取代空格
print('%010d' % 5)#0000000005
print('%-010d' % 5)#'5      '后面的没有用0来填充，因为填充后会变成很大的数字






























