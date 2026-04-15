class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        else :
            ds,dt = {},{}
            for i in range(len(s)) :
                ds[s[i]] = 1 + ds.get(s[i],0)
            for i in range(len(t)) :
                dt[t[i]] = 1 + dt.get(t[i],0)
            
            for i in ds :
                if ds[i] != dt.get(i,0) :
                    return False
            return True 
        