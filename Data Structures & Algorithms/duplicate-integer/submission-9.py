class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = set()
        for i in nums :
            if i in test :
                return True 
            else :
                test.add(i)
        return False