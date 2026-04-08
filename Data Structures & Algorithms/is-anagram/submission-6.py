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
            for i in s :
                ds[i] = 1 +  ds.get(i,0)
            for i in t :
                dt[i] = 1 +  dt.get(i,0) 
        for i in s :
            if ds[i] != dt.get(i,0):
                return False 
        return True

            

        