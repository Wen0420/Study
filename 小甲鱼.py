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