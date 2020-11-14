class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
#需要去overwrite之前的array
#3,2,2,3
#2,2,3,3
#for (int i = 0; i < 2; i++){
#   print(num[i]
#} 打印前两位

#这道题的逻辑
#3,2,2,3
#val = 3
#round 1_after_swap:3,2,2,3 第一位和最后一位调换，移去最后一位
#round 2_after_swap:2,2,3,3 指针现在指向第二位，第零位和第二位调换得到，现在指针指向第一位
#round 3_after_swap: 第零位是2 ，不做改变还是2,2,3,3
#round 4_after_swap: 去i+1位，第一位也是2，不做改变2,2,3,3
#round 5_after_swap: return last(指的是第一位的2) + 1就是想要的index 的长度

#首先定义一个指针一个是i, 一个是0

        i, last = 0, len(nums) - 1#array记数是从0开始的
        #while loop go though each element in the array
        while i <= last:
            #左边的指针一定要小于右边的，有交叠就是结束了
            #然后有两种一种是遇到的数字是想要删除的，另一种是不需要删除的
            #需要写个if else条件语句
            #如果第零位是我们想要删除的,就和最后一位swap
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                #然后减去最后一位，并不是真正意义上的删除
                last -= 1
            else:
                i += 1

        return last+1


