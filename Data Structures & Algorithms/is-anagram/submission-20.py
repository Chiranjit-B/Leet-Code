class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        if len(s) != len(t) :
            return False
        else :
            for i in range(len(s)) :
                ds[s[i]] = ds.get(s[i],0) + 1 
            for i in range(len(t)) :
                dt[t[i]] = dt.get(t[i],0) + 1

            for i in ds :
                if ds[i] != dt.get(i,0) :
                    return False
        return True


