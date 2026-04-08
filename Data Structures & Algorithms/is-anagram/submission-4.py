# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         ds,dt = {},{}
#         if len(s) != len(t) :
#             return False 
#         else :
#             for i in s :
#                 ds[s] = 1+ ds.get(s,0)
#             for i in t :
#                 dt[t] = 1+ dt.get(t,0)
            
#             for i in ds :
#                 if ds[i] != dt.get(i,0) :
#                     return False 
#         return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds,dt = {},{}
        if len(s) != len(t) :
            return False 
        else :
            for i in range (len(s)) :
                ds[s[i]] = 1+ ds.get(s[i],0)
                dt[t[i]] = 1+ dt.get(t[i],0)
            
            for i in ds :
                if ds[i] != dt.get(i,0) :
                    return False 
        return True
            

        