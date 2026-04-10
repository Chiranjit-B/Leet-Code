class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dis = set()
        for i in nums :
            if i in dis :
                return True
            dis.add(i)
        return False
        