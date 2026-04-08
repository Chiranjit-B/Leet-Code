class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test = {}
        for i, num in enumerate(nums) :
            x = target - num
            if x in test :
                return [test[x],i]
            test[num] = i 
        return []
    
                