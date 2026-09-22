class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        l = 2*len(nums)
        a = [0]*l
        for i in range(0,len(nums)) :
            a[i] = a[len(nums)+i] = nums[i]

        return a