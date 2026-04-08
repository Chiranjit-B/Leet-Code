class Solution:
    def hasDuplicate(self, arr: List[int]) -> bool:
        flag = 0
        b = []
        for i in arr :
            if i not in b :
                b.append(i)
            else :
                flag+=1
                break
        if flag >= 1 :
            return True
        else :
            return False
            
        