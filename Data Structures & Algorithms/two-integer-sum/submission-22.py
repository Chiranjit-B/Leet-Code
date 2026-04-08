class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test = {}
        for i, n in enumerate (nums):
            x = target - n 
            if x in test :
                return [test[x],i]
            test[n] = i
        return []
        