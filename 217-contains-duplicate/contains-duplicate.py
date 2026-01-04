class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for i in nums :
            if i not in dup :
                dup.add(i)
            else :
                return True
        return False
        