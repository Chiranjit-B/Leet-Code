class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in res :
                return [res[x],i]
            res[num] = i
        return []