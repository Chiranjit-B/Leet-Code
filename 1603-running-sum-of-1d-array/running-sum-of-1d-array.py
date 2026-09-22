class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = nums[0]
        for i in range(1,len(nums)) :
            sum+= nums[i]
            nums[i] = sum

        return nums
        