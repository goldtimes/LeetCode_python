#给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。
#不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。

class Solution():
    def removeDuplicates(self,nums):
        """
        :param nums: List[int]
        :return:int
        """
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if nums[i] == nums[j]:
                    del nums[i]

solution = Solution()
nums = [1,1,2]
solution.removeDuplicates(nums)
print(nums)