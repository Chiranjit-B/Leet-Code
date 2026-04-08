class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        d =  {}
        flag = 0
        for i in nums :
            d[i] = 0

    
        for i in nums :
            if i in d.keys() :
                d[i] += 1
        for i in d.values():
            if i > 1 :
                flag +=1
                break
      
        if flag == 1 :
            return True 
        else :
            return False
    
        

      
        

        