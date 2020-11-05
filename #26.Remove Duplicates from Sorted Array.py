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
