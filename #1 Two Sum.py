class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#法一
       #希望先遍历这个数组，去找到这两个数字,写个for loop去遍历里面所有的值
        for i in nums:
            j = target - i #两个数字
            start_index = nums.index(i)# i 所在的位置是start index
            next_index = start_index + 1 #下一个值是start index 的下一位，是不是它呢，需要做一个判断
            temp_nums = nums[next_index: ]#python做判断的时候可以新建立一个数组，然后这个数组是从next index 开始一直到结束
            #现在判断j 是不是在temp_nums:
            #如果是的话我们返回两个值，一个是开始的index（index number of i）, 一个是结束的index(next_index+这个值在tem array里面的位置)
            if j in temp_nums:
                return(nums.index(i), next_index + temp_nums.index(j))

#使用其他的办法优化这个算法，法二, two hash table
        dic = {}
        #还是想要遍历这个numbers
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                #我们想知道number of i 在不在这个dict 里面，如果是就直接return,如果不是就在这个dict里加一个num
                dict[nums[i]] = i
            else:
                return [dict[target-nums[i]], i]

#语法注释
len()
'''
1：作用：返回字符串、列表、字典、元组等长度

2：语法：len(str)

3：参数：
str：要计算的字符串、列表、字典、元组等

4：返回值：字符串、列表、字典、元组等元素的长度

5：实例
'''
#5.1、计算字符串的长度：
s = "hello good boy doiido"
print(len(s)) #21

#5.2、计算列表的元素个数：
l = ['h','e','l','l','o']
print(len(l)) #5

#5.3、计算字典的总长度(即键值对总数)：
d = {'num':123,'name':"doiido"}
print(len(d)) #2

#5.4、计算元组元素个数：
t = ('G','o','o','d')
print(len(t)) #4

range()
'''
python内置range()函数的作用是什么？它能返回一系列连续增加的整数，
它的工作方式类似于分片，可以生成一个列表对象。range函数大多数时常出现在for循环中，
在for循环中可做为索引使用。其实它也可以出现在任何需要整数列表的环境中，
在python 3.0中range函数是一个迭代器。

range (stop)
range (start,stop[ ,step])

start：计数从start开始，默认是从0开始。例如，range(5) 就相当于是range(0,5)

stop : 计数到stop结束，但不包括stop。例如:range(0,5)是 [0,1,2,3,4]

step:步长，默认为1，例如，range(0,5)等价于range(0,5,1)

for i in range ()作用：

range()是一个函数， for i in range () 就是给i赋值：
比如 for i in range （1，3）：
就是把1,2依次赋值给i

'''

#range()函数内只有一个参数，则表示会产生从0开始计数的整数列表：
i = range(4)
print(i)

for i in range(4):
    print(i)

for i in range(0,30,5):
    print(i)

c = list(range(0,30,5))
print(c)