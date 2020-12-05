#IDLE is Python's Integrated Development and Learning Environment.

#What can I do with python?
'''
https://realpython.com/what-can-i-do-with-python/
From web development to data science, machine learning, and more, Python’s real-world applications are limitless. However,As an interpreted language, Python has trouble interacting with low-level devices, like device drivers. For instance, you’d have a problem if you wanted to write an operating system with Python only. You’re better off sticking with C or C++ for low-level applications.
Pros:
#1: Automate the Boring Stuff
#2: Stay on Top of Bitcoin Prices
#3: Create a Calculator
#4: Mine Twitter Data
#5: Build a Microblog With Flask
#6: Build a Blockchain
#7: Bottle Up a Twitter Feed
#8: Play PyGames
#9: Choose Your Own Adventure
#10: Say “Hello World!” to Machine Learning
#11: Get Challenged
'''
#P1

#idle 交互模式，写一个代码，他会给你一个反馈
#idle 编辑模式：
print("Design the first game in python")

temp = input("Can you guess what number I have in mind?")
guess = int(temp)
if guess == 8:
    print()