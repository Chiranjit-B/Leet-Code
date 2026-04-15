class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dis = set()
        for i in nums :
            if i in dis :
                return True
            else :
                dis.add(i)
        return False
        