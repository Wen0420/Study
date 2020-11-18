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

