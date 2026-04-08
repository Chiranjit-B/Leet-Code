class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b = []
        flag = 0 
        for i in nums :
            if i not in b :
                b.append(i)
            elif i in b :
                flag += 1
                break 
        if flag == 1 :
            return True
        else :
            return False
        

        