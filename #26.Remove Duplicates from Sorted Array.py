class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #可能会存在nums里面没有任何数
        if not nums:
            return 0
        #接下来数数这个array里面有多少个不同的数字
        #在写for loop 前需要count, initial count 为0
        count = 0
        #遍历这个array 里所有的值
        for i in range(len(nums)):
            #count的是不同的值，如果值是一样的就不需要改变。只有两个值不一样才需要count+1
            if nums[count] != nums[i]:
                count +=1
                nums[count] = nums[i]
        return count +1

'''
Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
语法:
count()方法语法：
str.count(sub, start= 0,end=len(string))
参数:
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
返回值:
该方法返回子字符串在字符串中出现的次数。

例子:

'''
str = "this is string example....wow!!!";

sub = "i";
print("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))
sub = "wow";
print("str.count(sub) : ", str.count(sub))