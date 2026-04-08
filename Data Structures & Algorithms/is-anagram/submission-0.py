class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s) :
            return False
        else :
            ds = {}
            dt = {}
            for i in s :
                ds[i] = 0
            for i in t :   
                dt[i] = 0
            
            for i in s :
                ds[i] += 1
                
            for i in t :
                dt[i] += 1
            
            return (ds == dt)

        

        