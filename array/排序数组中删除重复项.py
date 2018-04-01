#给定一个有序数组，你需要原地删除其中的重复内容，使每个元素只出现一次,并返回新的长度。
#不要另外定义一个数组，您必须通过用 O(1) 额外内存原地修改输入的数组来做到这一点。

class Solution():
    def removeDuplicates(self,nums):
        """
        :param nums: List[int]
        :return:int
        """
        result = 1
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return 1
        for i in range(1,length):
            if nums[i - 1] == nums[i]:
                continue
            else:
                nums[result] = nums[i]
                result += 1
        return result

solution = Solution()
nums = [1,1,1,2,2,3,4,5,5,6]

result = solution.removeDuplicates(nums)
print(result)
print(len(nums))
for i in range(len(nums) - result):
    print(nums.pop())
print(nums)


