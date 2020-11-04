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

