class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0 
        j = 0
        ctr = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)) :
                if nums[i] == nums[j] :
                    print(nums[i], nums[j])
                    return True
        if ctr == 0 :
            return False 
            
        